RED SMS · Python
================

Требуется Python 3.8 или новее. Из корня репозитория::

    python3 -m venv .venv
    .venv/bin/python -m pip install .
    cp samples/config.json.dist samples/config.json

Для Windows используйте python из .venv/Scripts. В config.json укажите логин,
API-ключ, свой номер и зарегистрированные имена отправителей.

Проверка доступа и списка отправителей::

    .venv/bin/python samples/get_info.py
    .venv/bin/python samples/get_sender_name_list.py

Отправка одного платного SMS и проверка статуса::

    .venv/bin/python samples/send_sms.py

Скрипты send_viber.py и resend_sms_viber.py требуют подключенного канала Viber.
send_dispatch.py создаёт рассылку. Запускайте эти примеры с разрешёнными
для аккаунта именами и тестовым номером.

Документация: https://docs.redsms.ru/http/
