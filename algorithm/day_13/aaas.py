import sys

# 배열 크기, 개수, 이동 명령 횟수
N, M, K = map(int, sys.stdin.readline().split())

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

d = {}
ground = [[0] * N for _ in range(N)]
for di in range(M):
    i, j, mass, direction, speed = map(int, sys.stdin.readline().split())
    ground[i - 1][j - 1] = [mass, direction, speed]
    d[di + 1] = (i - 1, j - 1)
    # 5 2 2
    # 7 1 6
print(ground)
print(d) # {1: (0, 0), 2: (0, 3)}

for _ in range(K):
    for di in range(1, M + 1):
        i, j = d[di]
        mass, direction, speed = ground[i][j]
        i, j = (i + di[direction] * speed) % N, (j + dj[direction] * speed) % N
        print(i, j)