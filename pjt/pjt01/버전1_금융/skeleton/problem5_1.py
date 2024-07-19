import requests

API_KEY = 'd041d5b2deed53c8decf301f3fbadcb3'  # OpenWeatherMap API 키를 입력하세요.
CITY = 'Seoul'

def get_current_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def print_rain_info(data):
    if 'rain' in data:
        print(f"Current Rain (1h): {data['rain'].get('1h', 'No data')} mm")
    else:
        print("Current Rain: No rain data available")

# 현재 날씨 데이터 가져오기
current_weather = get_current_weather(API_KEY, CITY)
print("Current Weather:")
print_rain_info(current_weather)
