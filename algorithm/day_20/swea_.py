from collections import deque

def find_water(N, M):
    for i in range(N):
        for j in range(M):
            if beach[i][j] == 'W':
                for k in range(4):
                    mi, mj = i + di[k], j + dj[k]
                    if 0 <= mi < N and 0 <= mj < M and beach[mi][mj] == 'L':
                        bfs(i, j)
                        break

def bfs(si, sj):
    checked = [[0] * M for _ in range(N)]
    Q = deque()

    distance[si][sj] = 1
    checked[si][sj] = 1
    Q.append((si, sj))
    while Q:
        i, j = Q.popleft()
        for k in range(4):
            mi, mj = i + di[k], j + dj[k]
            if 0 <= mi < N and 0 <= mj < M and beach[mi][mj] != 'W' and checked[mi][mj] == 0:
                Q.append((mi, mj))
                checked[mi][mj] = 1
                temp_distance = distance[i][j] + 1
                if not distance[mi][mj]:
                    distance[mi][mj] = temp_distance
                elif distance[mi][mj]:
                    if distance[mi][mj] > temp_distance:
                        distance[mi][mj] = temp_distance


def cal_distance(N, M):
    s = 0
    for i in range(N):
        for j in range(M):
            if beach[i][j] == 'L':
                s += distance[i][j] - 1
    return s

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split()) # N 세로, M 가로
    beach = [list(input()) for _ in range(N)]
    distance = [[0] * M for _ in range(N)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    find_water(N, M)
    # print(distance)
    print(f'#{tc} {cal_distance(N, M)}')
