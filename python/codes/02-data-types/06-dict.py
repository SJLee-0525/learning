my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {
    'apple': 12, 
    'list': [1, 2, 3]
}
print(my_dict_1)  # {}
print(my_dict_2)  # {'key': 'value'}
print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}

my_dict = {'apple': 12, 'list': [1, 2, 3]}

# 값에 접근: 반드시 키를 사용해야 함
print(my_dict['apple']) # list = 인덱싱 / dict = 이름

# 추가
my_dict['banana'] = 50
print(my_dict)

# 변경
my_dict['banana'] = 1000 # 딕셔너리는 중복이 없기 때문에, 값이 업데이트 됨
print(my_dict)

#