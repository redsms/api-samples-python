import json
from pathlib import Path

from redsms import API

HERE = Path(__file__).resolve().parent


def settings():
    with (HERE / 'config.json').open(encoding='utf-8') as stream:
        config = json.load(stream)
    return config, API(config['login'], config['api_key'], config['phone_number'], config['default_sender'])


def result(response):
    try:
        body = response.json()
    except ValueError:
        raise SystemExit(f'HTTP {response.status_code}: expected JSON')
    if not response.ok or body.get('success') is False:
        raise SystemExit(f"HTTP {response.status_code}: {body.get('error_message', body)}")
    return body
