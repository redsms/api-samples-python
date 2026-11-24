#!/bin/env python
# encoding: utf-8

import json
import requests
from common import result, settings

def main():

    config, api = settings('phone_number', 'default_sender')

    body = {
        'route': 'sms',
        'from': config['default_sender'],
        'to': config['phone_number'],
        'name': 'Тестовая SMS-рассылка',
        'text': 'Тестовое сообщение от redsms.ru',
        'validity': api.VALIDITY_PERIOD_MAX,
    }

    info = api.post('dispatch', data=body)
    print(json.dumps(result(info), indent=2))

if __name__ == '__main__':
    try:
        main()
    except requests.RequestException as err:
        raise SystemExit(str(err))
