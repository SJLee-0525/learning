import requests
import pprint

# 서울의 위도 37.56 / 경도 126.97
lat = 37.56
lon = 126.97
api_key = 'd041d5b2deed53c8decf301f3fbadcb3'

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
response = requests.get(url).json()

pprint.pprint(response)
pprint.pprint(type(response))

c_temperture = float(response['main']['temp']) - 273.15
print(c_temperture)
