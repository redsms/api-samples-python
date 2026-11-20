#!/bin/env python
# encoding: utf-8

import json
import requests
from common import result, settings

def main():

    config, api = settings()
    test_number = config['phone_number']

    body = {
        'to': test_number,
        'text': 'This is a test for viber!',
        'from': config['viber_sender'],
        'sms.from': config['default_sender'],
        'route': 'viber,sms',
        'sms.text': 'This is a test for sms!',
        'viber.btnText': 'test_button',
        'viber.btnUrl': 'https://cp.redsms.ru/reports/details',
        'viber.validity': 10,
    }

    response = api.post('message', data=body)
    print(json.dumps(result(response), indent=2))

if __name__ == '__main__':
    try:
        main()
    except requests.RequestException as err:
        raise SystemExit(str(err))
