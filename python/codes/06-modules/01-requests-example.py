import requests

url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json() 
# requests의 .json이 딕셔너리로 전환해줌: 원래는 문자열임
# 요청, 응답, 변환 다 해주는 코드니 기억하기

print(type(response))
print(response)
