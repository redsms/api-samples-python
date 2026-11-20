#!/bin/env python
# encoding: utf-8

import json
import time

import requests

from common import result, settings

def main():

    config, api = settings()
    test_number = config['phone_number']

    body = {
        'text': 'Hello, world!',
        'to': test_number,
        'from': config['default_sender'],
        'route': 'sms',
    }

    response = api.post('message', data=body)

    body = result(response)
    if not body.get('items'):
        raise SystemExit(f"No accepted messages: {body.get('errors', [])}")
    messages = [message for message in body['items'] if message.get('uuid')]
    if not messages:
        raise SystemExit('Response contained no message UUID')
    for message in messages:
        print('{}: {}'.format(message['to'], message['uuid']))
        last_msg_uuid = message['uuid']

    print('Getting message info...')

    response = api.get('message/{}'.format(last_msg_uuid))
    print(json.dumps(result(response), indent=2))
    print('Waiting 10 seconds...')
    time.sleep(10)

    print('Getting message info again...')

    response = api.get('message/{}'.format(last_msg_uuid))
    print(json.dumps(result(response), indent=2))

if __name__ == '__main__':
    try:
        main()
    except requests.RequestException as err:
        raise SystemExit(str(err))
