for test_case in range(1, 11):
	T = int(input())

	arr = [list(map(int, input().split())) for _ in range(100)]

	# 행의 max값 구하기
	max_col_sum = 0
	for col in range(100):
		col_sum = 0
		for row in range(100):
			col_sum += arr[col][row]
		if max_col_sum < col_sum:
			max_col_sum = col_sum

	# 열의 max값 구하기
	max_row_sum = 0
	for row in range(100):
		row_sum = 0
		for col in range(100):
			row_sum += arr[col][row]
		if max_row_sum < row_sum:
			max_row_sum = row_sum

	# 11-5 방향 크로스 합 구하기
	cross_sum_1 = 0
	for col in range(100):
		for row in range(100):
			if col == row:
				cross_sum_1 += arr[col][row]

	# 7-1 방향 크로스 구하기
	cross_sum_2 = 0
	for col in range(100):
		for row in range(99, -1, -1):
			if col + row == 99:

				cross_sum_2 += arr[col][row]

	# 진짜 맥스 구하기
	real_max_sum = 0
	for max_sum in [max_col_sum, max_row_sum, cross_sum_1, cross_sum_2]:
		if real_max_sum < max_sum:
			real_max_sum = max_sum
	
	print(f'#{test_case} {real_max_sum}')












