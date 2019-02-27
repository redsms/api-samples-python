#!/bin/env python
# encoding: utf-8

import json
import requests
import redsms

def main():

    with open('config.json', 'r') as f:
        config = json.load(f)

    api = redsms.API(**config)
    test_number = '+79000000000'

    body = {
        'to': test_number,
        'text': 'This is a test for viber!',
        'from': 'NoName',
        'route': 'viber,sms',
        'sms.text': 'This is a test for sms!',
        'viber.btnText': 'test_button',
        'viber.btnUrl': 'https://cp.redsms.ru/reports/details',
        'viber.validity': 10,
    }

    response = api.post('message', data=body)
    print(json.dumps(response.json(), indent=2))

if __name__ == '__main__':
    try:
        main()
    except requests.exceptions.ConnectionError as err:
        print('Cannot connect to the server.')
