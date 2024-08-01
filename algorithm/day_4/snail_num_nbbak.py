T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 정사각형 배열의 크기
    arr = [[0] * N for _ in range(N)]

    i, j = 0, 0
    num = 1
    count = 0

    # 이 방법은 영 아닌 거 같은데,,,,
    while 1:
        while 1:
            arr[i][j] = num
            if j == N - count - 1:
                break
            num += 1
            j += 1
        if num == N * N:
            arr[i][j] = num
            break

        while 1:
            arr[i][j] = num
            if i == N - count - 1:
                break
            num += 1
            i += 1
        if num == N * N:
            arr[i][j] = num
            break

        while 1:
            arr[i][j] = num
            if j == count:
                break
            num += 1
            j -= 1
        if num == N * N:
            arr[i][j] = num
            break

        count += 1

        while 1:
            arr[i][j] = num
            if i == count:
                break
            num += 1
            i -= 1
        if num == N * N:
            arr[i][j] = num
            break

    print(f'#{test_case}')
    for mini_arr in arr:
        print(*mini_arr)