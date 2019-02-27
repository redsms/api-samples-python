# encoding: utf-8

from __future__ import unicode_literals

try:
    from collections.abc import Iterable, Mapping
except ImportError:
    from collections import Iterable, Mapping

try:
    unicode
except NameError:
    unicode = str

STRING_LIKE_TYPES = (str, bytes, bytearray, unicode)

def get_hashable_fields(data):
    reserved_keys = ('files', 'ts', 'login', 'secret')
    for key in data:
        if key not in reserved_keys:
            yield key

def stringify(value):
    if isinstance(value, Mapping):
        return {key: stringify(value) for key, value in value.items()}
    if isinstance(value, Iterable) and not isinstance(value, STRING_LIKE_TYPES):
        return ','.join(map(stringify, value))
    return unicode(value)
