"""
RedSms (c) 2018
Author: egzvor@gmail.com

RedSms Service Python API library
"""

import hashlib
import time
from functools import partial

import requests
from requests.compat import urljoin
from typing import Callable

# from .exceptions import RedSmsAPIError
from .utils import get_hashable_fields
from .utils import stringify


class API(object):
    """
    Simple wrapper class to use Red Sms REST API.
    """

    SMS_TYPE = 'sms'
    VIBER_TYPE = 'viber'
    RESEND_TYPE = 'viber,sms'
    VALIDITY_PERIOD_MIN = 60
    VALIDITY_PERIOD_MAX = 24 * 60 * 60

    API_URL = 'https://cp.redsms.ru/api/'

    def __init__(self, login, api_key, phone_number, default_sender):
        self._login = login
        self._api_key = api_key
        self._phone_number = phone_number
        self._default_sender = default_sender

        self._common_method_params = {
            'login': self._login,
            'User-Agent': 'RedSmsPythonLib',
        }

        self.session = requests.Session()
        self.session.headers['Accept'] = 'application/json'

    def __getattr__(self, httpmethod):
        try:
            method = getattr(self.session, httpmethod)
        except AttributeError:
            raise AttributeError('No such http method ({})!'.format(httpmethod))

        return partial(self.api_method, method)

    def _get_signature(self, timestamp, **data):
        md5_encoder = hashlib.md5()
        for key in sorted(get_hashable_fields(data)):
            md5_encoder.update(data[key].encode('utf-8'))
        md5_encoder.update(timestamp.encode('utf-8'))
        md5_encoder.update(self._api_key.encode('utf-8'))

        return md5_encoder.hexdigest()

    def api_method(self, method, url, data=None, files=None):
        # type: (Callable, str, dict, dict) -> requests.Response
        """
        Call http method with specified url and params
        """

        _url = urljoin(self.API_URL, url)
        params = self._common_method_params.copy()
        timestamp = stringify(time.time())
        string_params = stringify(data) if data else None
        sig = self._get_signature(timestamp, **(string_params or {}))
        params.update({
            'ts': timestamp,
            'sig': sig,
        })

        return method(_url, headers=params, data=string_params, files=files)
