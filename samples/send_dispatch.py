#!/bin/env python
# encoding: utf-8

import json
import requests
from common import result, settings

def main():

    config, api = settings()

    test_number = config['phone_number']

    text_viber = 'It is test for viber!'
    text_sms = 'It is test for sms!'
    dispatch_name = 'It is a test dispatch api'

    body = {
        'from': config['viber_sender'],
        'name': dispatch_name,
        'route': 'viber,sms',
        'sms.from': config['default_sender'],
        'sms.text': text_sms,
        'sms.validity': api.VALIDITY_PERIOD_MAX,
        'text': text_viber,
        'to': test_number,
        'validity': api.VALIDITY_PERIOD_MIN,
    }

    info = api.post('dispatch', data=body)
    print(json.dumps(result(info), indent=2))

if __name__ == '__main__':
    try:
        main()
    except requests.RequestException as err:
        raise SystemExit(str(err))
