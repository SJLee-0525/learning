# 1. Positional Arguments 위치 인자
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('sungjoon', 28)
greet(28, 'sungjoon') # 그저 위치에 전달하는 역할이기에 순서를 바꿔도 작동 문제 X

# greet('sungjoon') 
'''
값을 의도적으로 누락 
greet() missing 1 required positional argument: 'age'
'''

# 2. Default Argument Values 기본 인자 값
def greet_default(name, age = 15):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet_default('sungjoon', 28) # 값을 만약 전달한다면 기본값 대신 인자를 할당함
greet_default('sungjoon') # 값을 전달하지 않아도, 알아서 기본값 15를 할당함
 
# 3. Keyword Arguments 키워드 인자
def greet_kw(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet_kw(name = 'sungjoon', age = 28)
greet_kw(age = 33, name = 'seoho') 
# 매개변수와 인자의 위치를 일치시키지 않고 값을 할당할 수 있음
# 함수를 사용할 때 달라짐

'''greet_kw(age = 33,'seoho')'''
# positional argument follows keyword argument
# 키워드 인자는 반드시 위치 인자 뒤에 위치해야 함

# 4. Arbitrary Argument Lists 임의의 인자 목록
def calculate_sum(*args):
    print(args) # (1, 100, 500, 303): <class 'tuple'>
    
calculate_sum(1, 100, 500, 303)

# def calculate_sum(*args, params): 임의의 인자 뒤에 위치 인자 둘 수 없음
def calculate_sum_2(params, *args): # 이거는 가능
    print(params, ',', args)

calculate_sum_2(1, 100, 500, 303) # 1 , (100, 500, 303)

# 5. Arbitrary Keyword Argument Lists 임의의 키워드 인자 목록
def print_info(**kwargs):
    print(kwargs)

print_info(name = 'sungjoon', age = 28) # {'name': 'sungjoon', 'age': 28}

# 인자의 모든 종류를 적용한 예시

def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1) # 1
    print('pos2:', pos2) # 2
    print('default_arg:', default_arg) # 3
    print('args:', args) # (4, 5, 6)
    print('kwargs:', kwargs) # {key1='value1', key2='value2'}


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
