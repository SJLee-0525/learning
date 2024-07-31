datas = [0, 4, 1, 3, 1, 2, 4, 1, 9, 2, 150]
datas_len = 11
max_value = 150

# 최소값부터 최대값까지 전부 담을 수 있을 사이즈로 빈 counts 리스트 생성
counts = [0] * (max_value + 1)

# datas를 순회하면서 나오는 값을 counts의 인덱스로 삼아 1씩 더해줌
for data in datas:
	counts[data] += 1
print(counts) # [1, 3, 1, 1, 2]

# counts의 값을 누적 값으로 바꿔준다.
for i in range(1, len(counts)):
    counts[i] += counts[i - 1]
print(counts) # [1, 4, 5, 6, 8]

# 정렬할 값을 담을 temp list를 생성
temp = [0] * datas_len

# data의 값을 역순으로 가져와 해당 값과 같은 counts의 인덱스의 값을 1 감소시키고,
# 그 값을 temp의 인덱스로 해 data에서 가져온 값을 삽입.
for re_data in datas[::-1]:
	counts[re_data] -= 1
	temp[counts[re_data]] = re_data
print(temp) # [0, 1, 1, 1, 2, 3, 4, 4]