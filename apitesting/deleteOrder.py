import requests as rs

url = "https://simple-books-api.glitch.me/orders/pAZ49h3C_ddekVBPXFM7d"

my_header = {'Authorization': 'Bearer e7b41b6ee593899ef81cdca7fc2b29752f6b2baf224da5560245761691631829'}


def apiRequest():
    response = rs.delete(url, headers=my_header)
    print(response)


if __name__ == '__main__':
    apiRequest()
