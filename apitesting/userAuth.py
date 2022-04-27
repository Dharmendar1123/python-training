import json

import requests as rs

url = "https://simple-books-api.glitch.me/api-clients/"

user_data = {
    "clientName": 'Postman',
    "clientEmail": 'valentin1123@example.com'
}


def apiRequest():
    response = rs.post(url, json=user_data)
    objectToJson(response.json())


def objectToJson(data):
    my_response = json.dumps(data, indent=4)
    print(my_response)


if __name__ == "__main__":
    apiRequest()
