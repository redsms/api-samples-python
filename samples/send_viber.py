#!/bin/env python
# encoding: utf-8

from __future__ import unicode_literals

import json
import redsms
import requests
import sys
from pprint import pprint

def main():

    with open('config.json', 'r') as f:
        config = json.load(f)

    api = redsms.API(**config)
    test_number = config['phone_number']

    with open('data/images/REDSMS.png', 'rb') as f:
        files = {'file': f}
        response = api.post('storage', files=files)

    if response.json()['success'] == 'true':
        img_info = response.json()['items'][0]
    else:
        print('Cannot upload the image:')
        pprint(response.json())
        print('Here is your storage:')
        response = api.get('storage')
        pprint(response.json())
        sys.exit(1)

    body = {
        'text': 'Hello, Viber!',
        'to': test_number,
        'route': 'viber',
        'viber.btnText': 'Кнопка',
        'viber.btnUrl': 'https://cp.redsms.ru/',
        'viber.imageUrl': img_info['url'],
    }

    response = api.post('message', data=body)
    print(json.dumps(response.json(), indent=2))


if __name__ == '__main__':
    try:
        main()
    except requests.exceptions.ConnectionError:
        print('Cannot connect to the server.')
