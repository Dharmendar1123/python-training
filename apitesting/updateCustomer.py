import requests as rs

url = "https://simple-books-api.glitch.me/orders/Q6OPUxklVO0y5Sp-Cu30t"

my_header = {'Authorization': 'Bearer e7b41b6ee593899ef81cdca7fc2b29752f6b2baf224da5560245761691631829'}

user_data = {
    "customerName": "Akshay"
}


def apiRequest():
    response = rs.patch(url, headers=my_header, json=user_data)
    print(response)


if __name__ == '__main__':
    apiRequest()
