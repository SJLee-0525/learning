T = int(input())
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N - M + 1):
            for k in range(j, j + M):
                if arr[i][j + k] != arr[i][M - k - 1]:
                    break
            else:
                print(arr[i])
