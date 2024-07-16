my_range_1 = range(5)
my_range_2 = range(1, 10)
my_range_3 = range(9, 1, -2)
my_range_4 = range(0, 10, 2)
print(my_range_1)  # range(0, 5)
print(my_range_2)  # range(1, 10)
print(my_range_3)
print(my_range_4)

# 리스트로 형 변환 시 데이터 확인 가능
print(list(my_range_1))
print(list(my_range_2))
print(list(my_range_3))
print(list(my_range_4))

# 주로 반복문과 함께 활용
for i in range(5):
    print(i, end = '')

print('')

for j in range(0, 10, 3):
    print(j)