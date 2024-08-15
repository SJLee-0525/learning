T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split()) # 배열 크기, 단어 길이
    arr = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 2)]
    target = [0] + [1] * K + [0]

    cnt = 0
    for i in range(N + 2):
        for j in range(N - 2):
            if arr[i][j:j+K+2] == target:
                cnt += 1

    # 전치
    for ii in range(N + 2):
        for jj in range(N + 2):
            if ii < jj:
                arr[ii][jj], arr[jj][ii] = arr[jj][ii], arr[ii][jj]

    for i2 in range(N + 2):
        for j2 in range(N - 2):
            if arr[i2][j2:j2+K+2] == target:
                cnt += 1

    print(f'#{tc} {cnt}')