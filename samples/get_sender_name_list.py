#!/bin/env python
# encoding: utf-8

import json
import requests
from common import result, settings

def main():

    config, api = settings()

    info = api.get('sender-name')
    print(json.dumps(result(info), indent=2))


if __name__ == '__main__':
    try:
        main()
    except requests.RequestException as err:
        raise SystemExit(str(err))
