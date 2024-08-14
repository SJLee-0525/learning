from collections import deque

def find_start(N, maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def BFS(si, sj, N):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    while q:
        i, j = q.popleft()
        if maze[i][j] == 3:
            # print(visited)
            # print(q)
            return visited[i][j] - 2 # 경로의 빈 칸 수 (출발지 = 1, 도착지 = 1이기 떄문에 2 빼줌)
        for k in range(4):
            mi, mj = i + di[k], j + dj[k]
            if 0 <= mi < N and 0 <= mj < N and maze[mi][mj] != 1 and visited[mi][mj] == 0:
                q.append((mi, mj))
                visited[mi][mj] = visited[i][j] + 1
    return 0 # 도달 못하는 경우



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    si, sj = find_start(N, maze)
    print(f'#{tc} {BFS(si, sj, N)}')
