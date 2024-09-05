for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    target = [list(map(int, input().split())) for _ in range(3)]

    cnt = 0
    for i in range(N - 2):
        for j in range(N - 2):
            B = True
            for i2 in range(3):
                for j2 in range(3):
                    if arr[i + i2][j + j2] != target[i2][j2]:
                        B = False
                        break
                if B == False:
                    break
            if B == True:
                cnt += 1

    print(f'#{tc} {cnt}')