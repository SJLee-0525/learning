text = 'banana'

# find
print(text.find('a')) # 1
print(text.find('z')) # -1 : find 매서드는 해당 값이 없으면 -1을 반환

# index
print(text.index('a')) # 1
# print(text.index('z')) # ValueError: substring not found : index 매서드는 해당 값이 없으면 Error 발생

# isupper
string1 = 'HELLO'
string2 = 'Hello'
string3 = 'hello'

print(string1.isupper()) # True
print(string2.isupper()) # False
print(string3.isupper()) # False

# islower
print(string1.islower()) # False
print(string2.islower()) # False
print(string3.islower()) # True

# isalpha
alpha1 = 'Hello'
alpha2 = '123hello321abc'

print(alpha1.isalpha()) # True
print(alpha2.isalpha()) # False : 중간에 숫자가 섞였음

# replace
text = 'Hello, world!'

new_text_1 = text.replace('world', 'Python')
print(new_text_1) # Hello, Python!

text_2 = 'Hello, world world world!'
new_text_2 = text_2.replace('world', 'Python')
print(new_text_2) # Hello, Python Python Python! ([,count]를 지정하지 않으면 다 바꿔줌)

new_text_3 = text_2.replace('world', 'Python', 2)
print(new_text_3) # Hello, Python Python world! ([,count]는 바꿀 횟수임.)

# strip
text_4 = '  Hello, world!  '

new_text_4 = text_4.strip()
print(new_text_4) # Hello, world!

# split
text_5 = 'Hello, world!'

new_text_5 = text_5.split(',') 
print(new_text_5) # ['Hello', ' world!']

new_text_5_a = text_5.split(', ') 
print(new_text_5_a) # ['Hello', 'world!']

new_text_5_b = text_5.split()
print(new_text_5_b) # ['Hello,', 'world!'] : 구분자 지정 안하면 공백을 기준으로 나눔

# join
words = ['Hello', 'world!']

new_words = '-'.join(words)
print(new_words) # Hello-world!

# capitalize
text_6 = 'heLLo, woRld!'

new_text_6 = text_6.capitalize()
print(new_text_6) # Hello, world! : 첫 글자만 대문자로 바꿈

# title
new_text_7 = text_6.title()
print(new_text_7) # Hello, World! : 공백을 기준으로 첫 글자를 대문자로 바꿈

# upper
new_text_8 = text_6.upper()
print(new_text_8) # HELLO, WORLD! : 모두 대문자로

# lower
new_text_9 = text_6.lower()
print(new_text_9) # hello, world! : 모두 소문자로
 
# swapcase
new_text_10 = text_6.swapcase()
print(new_text_10) # HEllO, WOrLD! : 대문자 <-> 소문자 전환

# 참고
# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
print("isdecimal() 메서드 예시:")
print("'12345'.isdecimal():", '12345'.isdecimal())
print("'123.45'.isdecimal():", '123.45'.isdecimal())
print("'-123'.isdecimal():", '-123'.isdecimal())
print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())
print("'½'.isdecimal():", '½'.isdecimal())
print("'²'.isdecimal():", '²'.isdecimal())
print()

# isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
print("isdigit() 메서드 예시:")
print("'12345'.isdigit():", '12345'.isdigit())
print("'123.45'.isdigit():", '123.45'.isdigit())
print("'-123'.isdigit():", '-123'.isdigit())
print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())
print("'½'.isdigit():", '½'.isdigit())
print("'²'.isdigit():", '²'.isdigit())
print()

# isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
print("isnumeric() 메서드 예시:")
print("'12345'.isnumeric():", '12345'.isnumeric())
print("'123.45'.isnumeric():", '123.45'.isnumeric())
print("'-123'.isnumeric():", '-123'.isnumeric())
print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())
print("'½'.isnumeric():", '½'.isnumeric())
print("'²'.isnumeric():", '²'.isnumeric())

