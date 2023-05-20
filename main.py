import requests as req
import json

res = req.get('https://goweather.herokuapp.com/weather/kollam')
data = json.loads(res.text)
print(data)

temp = data.get('temperature')
wind = data.get('wind')
detail = data.get('description')

print(temp)
print(wind)
print(detail)
