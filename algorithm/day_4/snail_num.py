T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 정사각형 배열의 크기
    arr = [[0] * N for _ in range(N)]

    i, j, k = 0, 0, 0 # i는 row, j는 col, k는 di dj를 탐색하는데 사용할 인덱스

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 순회할 때 사용할 델타?

    for num in range(1, N * N + 1):
        arr[i][j] = num
        # 만약 다음 번에 사용할 인덱스가 인덱스 범위 내에 있고, 값이 0이라면 방향성을 유지함
        if 0 <= i + di[k] < N and 0 <= j + dj[k] < N and arr[i + di[k]][j + dj[k]] == 0:
            i += di[k]
            j += dj[k]
        # 아니라면 di, dj의 인덱스를 넘겨줌.
        else:
            k += 1
            # 만약 4를 넘어가면 0으로 초기화
            if k == 4:
                k = 0
            i += di[k]
            j += dj[k]

    print(f'#{test_case}')
    for mini_arr in arr:
        print(*mini_arr)