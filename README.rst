RED SMS · Python
================

Требуется Python 3.8 или новее. Из корня репозитория выполните::

    python3 -m venv .venv
    .venv/bin/python -m pip install .
    cp samples/config.json.dist samples/config.json

В Windows используйте ``.venv\Scripts\python.exe``. В ``samples/config.json``
укажите логин и API-ключ. Для отправки также укажите свой номер в международном
формате и зарегистрированное имя отправителя. Файл конфигурации исключён из Git.

Информация об аккаунте · GET /api/client/info::

    .venv/bin/python samples/get_info.py

Отправка одного платного SMS · POST /api/message::

    .venv/bin/python samples/send_sms.py

Проверка статуса · GET /api/message/{uuid}::

    .venv/bin/python samples/message_status.py UUID

После отправки возьмите UUID из ``items[0].uuid``. Передайте его в запрос статуса и прочитайте ``item.status``: значение ``delivered`` подтверждает доставку.

HTTP 200 подтверждает создание хотя бы
одного сообщения. При частичном принятии скрипт показывает UUID принятых
сообщений и ошибки по другим номерам. Доставку подтверждает статус
``delivered``. При ``created``, ``moderation`` и ``progress`` можно позже
повторить запрос статуса.

При HTTP 401 проверьте данные для подписи и список разрешённых IP.
При HTTP 420 проверьте баланс. При тайм-ауте отправки повторный POST может
создать дубликат.

Дополнительные примеры в ``samples`` показывают получение списка имён
отправителей и создание SMS-рассылки.

`Справочник HTTP API <https://docs.redsms.ru/http/api/>`_
· `Статусы сообщений <https://docs.redsms.ru/http/api/message/>`_
