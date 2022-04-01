import requests as rs
import json

response = rs.get("http://api.open-notify.org/astros.json")
# print(response.status_code)
# print(response.json())
# print((response.text))


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    # print(type(text))
    print(text)


jprint(response.json())
