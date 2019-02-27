#!/bin/env python
# encoding: utf-8

import json
import requests
import redsms

def main():

    with open('config.json', 'r') as f:
        config = json.load(f)

    api = redsms.API(**config)

    test_number = config['phone_number']

    text_viber = 'It is test for viber!'
    text_sms = 'It is test for sms!'
    dispatch_name = 'It is a test dispatch api'

    body = {
        'from': 'ABCP',
        'name': dispatch_name,
        'route': 'viber,sms',
        'sms.from': 'REDSMS.RU',
        'sms.text': text_sms,
        'sms.validity': api.VALIDITY_PERIOD_MAX,
        'text': text_viber,
        'to': test_number,
        'validity': api.VALIDITY_PERIOD_MIN,
    }

    info = api.post('dispatch', data=body)
    print(json.dumps(info.json(), indent=2))

if __name__ == '__main__':
    try:
        main()
    except requests.exceptions.ConnectionError as err:
        print('Cannot connect to the server.')
