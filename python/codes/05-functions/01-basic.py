def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2

result = make_sum(100, 30)
print(result)

return_value = print(result) # 여기서 130이 한 번 더 출력됨.
print(return_value) 
# None 출력 -> print 함수는 return이 없다.
# 출력과 리턴은 다름
# 리턴은 반환되는 값이 있고, **할당할 수 있음**
# 출력은 반환되는 값이 없고 그저 출력할 뿐임.

def my_func():
    print('hello world')

result_2 = my_func()
print(result_2)
# hello world
# None
# 두 줄이 출력됨. 
# 함수 내에서 출력이 일어났지만, 반환된 값은 없기 때문
