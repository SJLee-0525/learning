def kill_fly(i, j, N, M):
    di = [1, 0, -1 ,0]
    dj = [0, 1, 0, -1]

    kill_cnt = flies[i][j]

    for k in range(4):
        for l in range(1, M): # 표기 강도가 3이지만 실제로는 2칸씩만 쏴야 하니까 인덱스 조정
            mi, mj = i + (di[k] * l), j + (dj[k] * l)
            if 0 <= mi < N and 0 <= mj < N:
                kill_cnt += flies[mi][mj]

    return kill_cnt

def kill_fly_cross(i, j, N, M):
    di = [1, -1, -1, 1]
    dj = [1, 1, -1, -1]

    kill_cnt = flies[i][j]

    for k in range(4):
        for l in range(1, M):
            mi, mj = i + (di[k] * l), j + (dj[k] * l)
            if 0 <= mi < N and 0 <= mj < N:
                kill_cnt += flies[mi][mj]

    return kill_cnt

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N 배열크기 / M 강도
    flies = [list(map(int, input().split())) for _ in range(N)]
    # kills = [[0] * N for _ in range(N)]

    max_kill = -1
    for i in range(N):
        for j in range(N):
            result = max(kill_fly(i, j, N, M), kill_fly_cross(i, j, N, M))
            if max_kill < result:
                max_kill = result

    print(f'#{tc} {max_kill}')



