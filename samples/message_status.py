import json
import re
import sys

import requests

from common import result, settings


def main():
    if len(sys.argv) != 2 or not re.fullmatch(r"[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}", sys.argv[1], re.I):
        raise SystemExit("Использование: python samples/message_status.py UUID")

    _, api = settings()
    response = api.get(f"message/{sys.argv[1]}", data={"fields": "uuid,status,errCode"})
    print(json.dumps(result(response), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except requests.RequestException as error:
        raise SystemExit(str(error))
