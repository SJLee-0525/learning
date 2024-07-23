'# clear'
person_1 = {'name': 'Alice', 'age': 25}

person_1.clear()
print(person_1)

'# get'
person_2 = {'name': 'Alice', 'age': 25}

# 대괄호를 이용한 표기와 get 매서드는 비슷하게 해당 키에 대한 값을 반환하는 역할을 수행함
print(person_2.get('name')) # Alice
print(person_2['name']) # Alice

# 하지만 둘의 차이는 해당 키가 없을 때 발생함: get의 경우 None, 대괄호의 경우 오류
print(person_2.get('country')) # None
# print(person_2['country']) # KeyError: 'country'

# get()의 경우 선택 인자를 삽입하면, key가 없을 때 반환할 기본 값을 지정할 수 있음.
print(person_2.get('country', 'Korea')) # Korea
print(person_2) # {'name': 'Alice', 'age': 25}

'# keys'
person_3 = {'name': 'Alice', 'age': 25}

print(person_3.keys()) # dict_keys(['name', 'age']) : <class 'dict_keys'> 

'# values'
person_4 = {'name': 'Alice', 'age': 25}

print(person_4.values()) # dict_values(['Alice', 25]) : <class 'dict_values'>

'# items'
person_5 = {'name': 'Alice', 'age': 25}

print(person_5.items()) # dict_items([('name', 'Alice'), ('age', 25)]) : <class 'dict_items'>

'# pop'
person_6 = {'name': 'Alice', 'age': 25}

# pop 매서드 안의 key와 연관된 value를 반환하고, 해당 key - value 쌍을 제거
print(person_6.pop('name')) # Alice
print(person_6) # {'age': 25}

# pop 매서드 안의 key가 없으면 오류 발생 / 기본 값을 준다면 기본 값을 출력함
# print(person_6.pop('country')) # KeyError: 'country'
print(person_6.pop('country', '값이 없음')) # 값이 없음

'# setdefault'
person_7 = {'name': 'Alice', 'age': 25}

# key가 있다면 get()과 같음.
print(person_7.setdefault('country', 'KOREA')) # KOREA
print(person_7) # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

print(person_7.setdefault('name', 'sungjoon')) # Alice
print(person_7) # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

'# update'
person_8 = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person_8.update(other_person) 
print(person_8) # # {'name': 'Jane', 'age': 25, 'gender': 'Female'}
print(other_person) # {'name': 'Jane', 'gender': 'Female'} : 기존 키는 그대로 유지

# 키워드 인자도 가능
person_8.update(age = 50, country = 'Korea') 
print(person_8)
# {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'Korea'}


'업데이트를 했을 때 복사의 종류는?'
a = {}
b = {'name': 'Jane', 'gender': 'Female'}

a.update(b)

print(a) # {'name': 'Jane', 'gender': 'Female'}
b['name'] = 'sungjoon'

print(a) # {'name': 'Jane', 'gender': 'Female'}
print(b) # {'name': 'sungjoon', 'gender': 'Female'}
'''
서로 영향을 주지 않음. dict를 생성할 때 서로 다른 주소를 가지고 생성되기 때문임 
'''