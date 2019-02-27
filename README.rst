Simple API wrapper for redsms_ service
--------------------------------------

This is a python library that wraps RedSms API.

Supported version
=================

Both Python 2 and 3 are supported.

Installation
============

Use ``virtualenv`` to install ``redsms`` package.

.. highlight: sh

::

   virtualenv --python <path/to/the/preffered/version> .env
   source .env/bin/activate
   python setup.py install

Configuration
=============

To use the API you need to register at https://cp.redsms.ru and specify API key in settings. Copy sample config file. And fill out the necessary information.

::

   cp samples/sample.config.json samples/config.json

Example Usage
=============

See example scripts in the ``samples`` directory.

::

   source .env/bin/activate
   cd samples
   python get_info.py

**NB:** The regular price will be charged from your account.

Call for contributions
======================

This is an open source project. Your ideas to improve the library are welcome.

.. _redsms: https://cp.redsms.ru/
