#!/bin/env python
# encoding: utf-8

import json
import requests
import redsms

def main():

    with open('config.json', 'r') as f:
        config = json.load(f)

    api = redsms.API(**config)

    info = api.get('client/info')
    print(json.dumps(info.json(), indent=2))


if __name__ == '__main__':
    try:
        main()
    except requests.exceptions.ConnectionError as err:
        print('Cannot connect to server.')
