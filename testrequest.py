import requests

url = 'http://apiprod.cuik.io/'

response = requests.get(url)
print(response.status_code)
print(response.text)
