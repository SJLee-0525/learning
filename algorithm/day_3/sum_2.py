for test_case in range(1, 11):
    T = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

	# 행의 max값 구하기

    max_row_sum = 0
    max_col_sum = 0
    cross_1 = 0
    cross_2 = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
            if i == j:
                cross_1 += arr[i][j]
            elif i + j == 99:
                cross_2 += arr[i][j]
        if max_row_sum < row_sum:
            max_row_sum = row_sum
        if max_col_sum < col_sum:
            max_col_sum = col_sum

    max_list = [max_row_sum, max_col_sum, cross_1, cross_2]
    real_max = 0
    for max_value in max_list:
        if real_max < max_value:
            real_max = max_value

    print(f'#{test_case} {real_max}')