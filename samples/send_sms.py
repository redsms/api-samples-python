#!/bin/env python
# encoding: utf-8

import json
import time

import requests

import redsms

def main():

    with open('config.json', 'r') as f:
        config = json.load(f)

    api = redsms.API(**config)
    test_number = '+79000000000'

    body = {
        'text': 'Hello, world!',
        'to': test_number,
    }

    response = api.post('message', data=body)

    for message in response.json()['items']:
        print('{}: {}'.format(message['to'], message['uuid']))
        last_msg_uuid = message['uuid']

    print('Getting message info...')

    response = api.get('message/{}'.format(last_msg_uuid))
    print(json.dumps(response.json(), indent=2))
    print('Waiting 10 seconds...')
    time.sleep(10)

    print('Getting message info again...')

    response = api.get('message/{}'.format(last_msg_uuid))
    print(json.dumps(response.json(), indent=2))

if __name__ == '__main__':
    try:
        main()
    except requests.exceptions.ConnectionError as err:
        print('Cannot connect to the server.')
