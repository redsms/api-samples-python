#!/bin/env python
# encoding: utf-8

import json
import time
import sys

import requests

from common import result, settings

def main():

    config, api = settings()
    test_number = config['phone_number']

    body = {
        'text': 'Тестовое сообщение от redsms.ru',
        'to': test_number,
        'from': config['default_sender'],
        'route': 'sms',
    }

    response = api.post('message', data=body)

    body = result(response)
    errors = body.get('errors', [])
    if errors:
        print(json.dumps(errors, ensure_ascii=False), file=sys.stderr)
    pending = set()
    for item in body.get('items', []):
        if not item.get('uuid'):
            raise SystemExit('Missing message UUID')
        print(f"{item['to']}: {item['uuid']}")
        pending.add(item['uuid'])
    if not pending:
        raise SystemExit('No accepted messages')

    failed = bool(errors)
    for attempt in range(2):
        if not pending:
            break
        if attempt:
            time.sleep(10)
        for uuid in sorted(pending):
            response = api.get(f'message/{uuid}', data={'fields': 'uuid,status,errCode'})
            item = result(response).get('item', {})
            status = item.get('status')
            if not status:
                raise SystemExit(f'{uuid}: missing status')
            print(f"{uuid}: {status}, errCode={item.get('errCode')}")
            if status not in ('created', 'moderation', 'progress'):
                pending.remove(uuid)
                if status != 'delivered':
                    failed = True
    if pending:
        print('Check these UUIDs again later:', ', '.join(sorted(pending)))
    if failed:
        raise SystemExit(1)


if __name__ == '__main__':
    try:
        main()
    except requests.RequestException as err:
        raise SystemExit(str(err))
