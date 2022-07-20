#Weather api

import requests

api_key = '6a3dfd99dd2627a1eddb40c7deff6b3b'
city = 'Orlando'
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q='+city+'&appid='+api_key

requests = requests.get(url)
json = requests.json()
print(json)