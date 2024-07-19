import requests
import pprint

city_name = 'Seoul,KR' # 'Tokyo,JP', 'New York,US'
api_key = 'd041d5b2deed53c8decf301f3fbadcb3'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

response = requests.get(url).json()


pprint.pprint(response.keys())