T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    for ii in range(N): # 가장 왼쪽에 1 할당
        arr[ii][0] = 1

    for i in range(1, N): # 해당 arr 값은 왼쪽 상단과 바로위의 값을 더한 것임
        for j in range(1, N):
            arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]

    print(f'#{tc}') # 출력 하기
    for a in range(N):
        for b in range(N):
            if arr[a][b] != 0:
                print(arr[a][b], end = ' ')
        print()
