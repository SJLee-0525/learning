my_range_1 = range(5)
my_range_2 = range(1, 10)
my_range_3 = range(9, 1, -2)
my_range_4 = range(0, 10, 2)
print(my_range_1)  # range(0, 5)
print(my_range_2)  # range(1, 10)
print(my_range_3)  # range(9, 1, -2)
print(my_range_4)  # range(0, 10, 2)

# 리스트로 형 변환 시 데이터 확인 가능
print(list(my_range_1)) # [0, 1, 2, 3, 4]
print(list(my_range_2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(my_range_3)) # [9, 7, 5, 3]
print(list(my_range_4)) # [0, 2, 4, 6, 8]

# 주로 반복문과 함께 활용
for i in range(5):
    print(i, end = '')

print('')
# 01234

for j in range(0, 10, 3):
    print(j)
    '''
    0
    3
    6
    9
    '''