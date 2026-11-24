#!/bin/env python
# encoding: utf-8

import json
import re
import sys

import requests

from common import result, settings

def main():

    config, api = settings('phone_number', 'default_sender')
    test_number = config['phone_number']
    if not re.fullmatch(r'[+]?[1-9][0-9]{1,14}', test_number):
        raise SystemExit('Укажите один номер в международном формате, например +12025550123.')

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
    items = body.get('items', [])
    if not items:
        raise SystemExit('Сервер не принял ни одного сообщения')
    for item in items:
        if not item.get('uuid'):
            raise SystemExit('В ответе отсутствует UUID сообщения')
        print(f"{item.get('to', test_number)}: {item['uuid']}")
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    try:
        main()
    except requests.RequestException as error:
        raise SystemExit(str(error))
