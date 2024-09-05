for tc in range(1, int(input()) + 1):
    N = int(input())
    i1, j1, i2, j2 = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]

    t = 0
    c = 0
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            t += ground[i][j]
            c += 1

    std = t // c

    rst = 0
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            rst += abs(ground[i][j] - std)

    print(f'#{tc} {rst}')