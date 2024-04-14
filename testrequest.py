import requests

url = 'https://nemzy.cuik.io/hello'

response = requests.get(url)
print(response.status_code)
print(response.text)
