import requests as rs
import json

url = "https://simple-books-api.glitch.me/books"

parameters = {
    "type": "non-fiction",
    # "limit": 1
}

def apiRequest():
    response = rs.get(url, params=parameters)
    listToString(response)


def listToString(data):
    response_data = json.dumps(data.json(), indent=4)
    print(response_data)


if __name__ == "__main__":
    apiRequest()
