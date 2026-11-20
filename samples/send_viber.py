#!/bin/env python
# encoding: utf-8

from __future__ import unicode_literals

import json
from common import HERE, result, settings
import requests
import sys
from pprint import pprint

def main():

    config, api = settings()
    test_number = config['phone_number']

    with (HERE / 'data/images/REDSMS.png').open('rb') as f:
        files = {'file': f}
        response = api.post('storage', files=files)

    uploaded = result(response)
    if uploaded.get('items'):
        img_info = uploaded['items'][0]
    else:
        print('Cannot upload the image:')
        pprint(result(response))
        print('Here is your storage:')
        response = api.get('storage')
        pprint(result(response))
        sys.exit(1)

    body = {
        'text': 'Тестовое сообщение от redsms.ru',
        'to': test_number,
        'route': 'viber',
        'from': config['viber_sender'],
        'viber.btnText': 'Кнопка',
        'viber.btnUrl': 'https://cp.redsms.ru/',
        'viber.imageUrl': img_info['url'],
    }

    response = api.post('message', data=body)
    print(json.dumps(result(response), indent=2))


if __name__ == '__main__':
    try:
        main()
    except requests.RequestException as err:
        raise SystemExit(str(err))
