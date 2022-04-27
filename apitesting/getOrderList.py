import json
import requests as rs

url = "https://simple-books-api.glitch.me/orders"

my_header = {'Authorization': 'Bearer e7b41b6ee593899ef81cdca7fc2b29752f6b2baf224da5560245761691631829'}


def apiRequest():
    response = rs.get(url, headers=my_header)
    apiToString(response.json())

def apiToString(data):
    my_response = json.dumps(data, indent=4)
    print(my_response)


if __name__ == "__main__":
    apiRequest()
