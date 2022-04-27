import requests as rs
import json

url = "https://simple-books-api.glitch.me/orders/Q6OPUxklVO0y5Sp-Cu30t"

my_header = {'Authorization': 'Bearer e7b41b6ee593899ef81cdca7fc2b29752f6b2baf224da5560245761691631829'}


def apiRequest():
    response = rs.get(url, headers=my_header)
    objectToJson(response.json())


def objectToJson(data):
    my_response = json.dumps(data, indent=4)
    print(my_response)


if __name__ == '__main__':
    apiRequest()
