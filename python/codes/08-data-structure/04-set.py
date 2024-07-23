'# add'
my_set_1 = {'a', 'b', 'c', 1, 2, 3}

# 값이 없을 경우 추가
my_set_1.add('d')
print(my_set_1) # {'a', 1, 2, 3, 'c', 'b', 'd'}

# 이미 값이 있을 경우 변화 X
my_set_1.add(1)
print(my_set_1) # {'a', 1, 2, 3, 'c', 'b', 'd'}

'# clear'
my_set_2 = {'a', 'b', 'c', 1, 2, 3}

my_set_2.clear()
print(my_set_2) # set() : 빈 세트는 중괄호로 표기 X, 함수 형태로 

'# remove'
my_set_3 = {'a', 'b', 'c', 1, 2, 3}

# 해당 값을 제거
my_set_3.remove('a')
print(my_set_3) # {1, 2, 3, 'b', 'c'}

'해당 값이 없다면, Error 발생'
# my_set_3.remove('가')
# print(my_set_3) # KeyError: '가'

'# pop'
my_set_4 = {'a', 'b', 'c', 1, 2, 3}

elem = my_set_4.pop()
print(elem, my_set_4) # 1 {2, 3, 'a', 'c', 'b'} / b {2, 3, 1, 'c', 'a'} / c {1, 2, 3, 'b', 'a'}

'# discard'
my_set_5 = {'a', 'b', 'c', 1, 2, 3}

# .remove()와 동일하게 해당 값을 제거
my_set_5.discard(1)
print(my_set_5) # {2, 3, 'b', 'a', 'c'}

'리스트와 달리 Error 없음'
my_set_5.discard(10)
print(my_set_5) # {2, 3, 'b', 'a', 'c'}

'# update'
my_set_6 = {'a', 'b', 'c', 1, 2, 3}

'list의 extend()와 비슷'
my_set_6.update([1, 4, 5, 6])
print(my_set_6) # {1, 2, 3, 4, 'b', 5, 6, 'c', 'a'}

'# 집합 메서드'
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

# 차집합 : -
print(set1.difference(set2)) # {0, 2, 4}

# 교집합 : &
print(set1.intersection(set2)) # {1, 3}

# 합집합 : |
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}

# 포함 여부: >=
print(set1.issubset(set2)) # False 
print(set3.issubset(set1)) # True

# 포함 여부 : <=
print(set1.issuperset(set2)) # False
print(set1.issuperset(set3)) # True