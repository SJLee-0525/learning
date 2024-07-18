# 사용 전
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)


# 사용 후
squared_numbers_2 = [num ** 2 for num in numbers]
print(squared_numbers_2)

# if문 포함
squared_numbers_3 = [num ** 2 for num in numbers if num % 2 == 1]
print(squared_numbers_3)

# List Comprehension 활용 예시 - "2차원 배열 생성 시 (인접행렬 생성 시)"
data1 = [[0] * (5) for _ in range(5)]
print(data1)

# 또는 (중첩 List Comprehension)
data2 = [[0 for _ in range(5)] for _ in range(5)]
print(data2)
