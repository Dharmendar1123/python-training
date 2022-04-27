import requests as rs

url = "https://simple-books-api.glitch.me/status"


def apiRequest():
    response = rs.get(url)
    print(type(response))
    if response.json()['status'] == 'OK':
        print("Status OK")
    else:
        print("Something went wrong")


if __name__ == "__main__":
    apiRequest()
