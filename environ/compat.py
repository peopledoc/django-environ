# -*- coding: utf-8 -*-

"""
environ.compat
~~~~~~~~~~~~~~~
This module handles import compatibility issues between Python 2 and
Python 3.
"""

import sys
import pkgutil

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

try:
    import urllib.parse as urlparselib
    quote = urlparselib.quote  # noqa
    unquote_plus = urlparselib.unquote_plus  # noqa
    basestring = str
except ImportError:
    import urlparse as urlparselib
    from urllib import quote, unquote_plus  # noqa
    basestring = basestring


urlparse = urlparselib.urlparse
urlunparse = urlparselib.urlunparse
ParseResult = urlparselib.ParseResult
parse_qs = urlparselib.parse_qs


try:
    import simplejson as json
except ImportError:
    import json  # noqa


try:
    from django import VERSION as DJANGO_VERSION
    from django.core.exceptions import ImproperlyConfigured  # noqa
except ImportError:
    DJANGO_VERSION = None

    class ImproperlyConfigured(Exception):
        pass


# back compatibility with django postgresql package
if DJANGO_VERSION is not None and DJANGO_VERSION < (2, 0):
    DJANGO_POSTGRES = 'django.db.backends.postgresql_psycopg2'
else:
    # https://docs.djangoproject.com/en/2.0/releases/2.0/#id1
    DJANGO_POSTGRES = 'django.db.backends.postgresql'

# back compatibility with redis_cache package
if pkgutil.find_loader('redis_cache'):
    REDIS_DRIVER = 'redis_cache.RedisCache'
else:
    REDIS_DRIVER = 'django_redis.cache.RedisCache'
