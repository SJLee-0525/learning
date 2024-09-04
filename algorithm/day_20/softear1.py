import sys

def dfs(i, j, m, M, visited=None):
    '''(입력 좌표, 바라보는 좌표 인덱스, 좌표 리스트 길이, visited)'''
    global cnt

    if visited == None: # 초기 생성시 visited가 없으면 만들고 방문표시
        visited = [[0] * N for _ in range(N)]
        visited[i][j] = 1
    print(visited, '현재 위치:', (i, j), '목표 좌표 정보:', m, route[m])

    if arr[i][j] == 9:  # 만약 방문지점에 도착하면
        if (i, j) == route[m]:  # 순서에 맞는지 검사후 맞으면
            m += 1              # 좌표 인덱스 변경
            if m == M:          # 좌표 인덱스가 길이랑 같아지면 (끝까지 도착)
                cnt += 1        # 카운트 증가 후 리턴
                print('도착')
                return
        else:                   # 순서에 맞지 않으면
            return              # 더 돌 필요 없이 리턴

    # 델타 순회
    for k in range(4):
        mi, mj = i + di[k], j + dj[k]
        # 인덱스 범위를 벗어나지 않고, 벽이 아니며 방문한 적이 없다면
        if 0 <= mi < N and 0 <= mj < N and arr[mi][mj] != 1 and visited[mi][mj] == 0:
            visited[mi][mj] = 1         # 이동할 좌표 방문 표시 해주고
            dfs(mi, mj, m, M, visited)  # 이동한 좌표로 재귀 탐색
            visited[mi][mj] = 0         # 돌아오면 방문 표시 지움


N, M = map(int, sys.stdin.readline().split()) # 격자 크기 방문해야 하는 칸 수
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
route = [] # [(2, 0), (0, 1), (1, 2)]

for _ in range(M): # 좌표 리스트에 인덱스 삽입
    x, y = map(int, sys.stdin.readline().split())
    x -= 1      # 인덱스 값에 맞게 변경
    y -= 1
    route.append((x, y))

# 가야할 좌표는 지도에 따로 표시
for x, y in route:
    arr[x][y] = 9

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
cnt = 0

dfs(route[0][0], route[0][1], 0, M)

print(cnt)


