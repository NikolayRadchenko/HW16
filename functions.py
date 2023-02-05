import json


def get_response(data) -> json:
    return json.dumps(data), 200, {'Content-Type': 'application/json; charset=utf-8'}