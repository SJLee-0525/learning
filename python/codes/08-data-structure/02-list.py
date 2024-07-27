# append
my_list = [1, 2, 3]

my_list.append(4)
print(my_list) # [1, 2, 3, 4]
print(my_list.append(4)) # None : 리스트 관련된 매서드는 반환 값이 없음.

# extend
my_list_2 = [1, 2, 3]

my_list_2.extend([4, 5, 6])
print(my_list_2) # [1, 2, 3, 4, 5, 6] : iterable한 객체를 풀어서 넣음

my_list_2.append([4, 5, 6])
print(my_list_2) # [1, 2, 3, 4, 5, 6, [4, 5, 6]] : list 안에 list 삽입하려면 append 사용

# my_list_2.extend(5)
# print(my_list_2) # TypeError: 'int' object is not iterable

# insert
my_list_3 = [1, 2, 3]

my_list_3.insert(1, 100)
print(my_list_3) # [1, 100, 2, 3] : 1번 index에 100을 삽입

# remove
my_list_4 = [1, 2, 3, 2, 3, 2]

my_list_4.remove(2)
print(my_list_4) # [1, 3, 2, 3, 2] : 해당되는 값 중 첫번째의 것을 제거함

# pop
my_list_5 = [1, 2, 3, 4, 5]

item_1 = my_list_5.pop()
print(item_1, my_list_5) # 5 [1, 2, 3, 4] : 리스트의 가장 마지막 요소가 제거된 후 item_1에 반환

item_2 = my_list_5.pop(0)
print(item_2, my_list_5) # 1 [2, 3, 4] : 리스트의 0번째 요소가 제거된 후 item_2에 반환
 
# clear
my_list_6 = [1, 2, 3]

my_list_6.clear()
print(my_list_6) # []
 
# index
my_list_7 = [1, 2, 3]

index = my_list_7.index(2)
# index = my_list_7.index(4) 문자열 index와 같이 없으면 오류 발생

print(index) # 1 : 해당되는 요소들 중 가장 왼쪽의 것의 인덱스를 반환

# count
my_list_8 = [1, 2, 2, 3, 3, 3]

counting_number = my_list_8.count(3)
print(counting_number) # 3 : 해당되는 요소의 개수를 반환

# reverse
my_list_9 = [1, 3, 2, 8, 1, 9]

my_list_9.reverse()
print(my_list_9) # [9, 1, 8, 2, 3, 1] : 원본 리스트를 역순으로 변경 (반환 X)

# sort
my_list_10 = [3, 2, 100, 1]

my_list_10.sort()
print(my_list_10) # [1, 2, 3, 100] : 오름차순으로 정렬 (반환 X)

# sort(내림차순 정렬)
my_list_10.sort(reverse=True)
print(my_list_10) # [100, 3, 2, 1] : 내림차순으로 정렬 (반환 X)