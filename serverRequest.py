import requests

x = requests.get('http://localhost:30000/')

print(x.text)