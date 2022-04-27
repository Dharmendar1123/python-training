import json
import requests as rs

url = "https://simple-books-api.glitch.me/orders"

my_headers = {'Authorization': 'Bearer e7b41b6ee593899ef81cdca7fc2b29752f6b2baf224da5560245761691631829'}

my_data = {
    "bookId": 1,
    "customerName": "hritik"
}


def apiRequest():
    response = rs.post(url, headers=my_headers, json=my_data)
    apiToString(response.json())

def apiToString(data):
    my_response = json.dumps(data, indent=4)
    print(my_response)


if __name__ == '__main__':
    apiRequest()
