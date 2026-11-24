import json
from pathlib import Path

from redsms import API

HERE = Path(__file__).resolve().parent


def settings(*required):
    with (HERE / 'config.json').open(encoding='utf-8') as stream:
        config = json.load(stream)
    for field in ('login', 'api_key', *required):
        if not isinstance(config.get(field), str) or not config[field].strip():
            raise SystemExit(f'Заполните {field} в samples/config.json')
    return config, API(config['login'], config['api_key'])


def result(response):
    try:
        body = response.json()
    except ValueError:
        raise SystemExit(f'HTTP {response.status_code}: expected JSON')
    if not isinstance(body, dict):
        raise SystemExit(f'HTTP {response.status_code}: expected a JSON object')
    if response.status_code != 200 or body.get('success') is False:
        message = body.get('error_message', 'Request failed')
        if body.get('errors'):
            message += ' ' + json.dumps(body['errors'], ensure_ascii=False)
        raise SystemExit(f'HTTP {response.status_code}: {message}')
    return body
