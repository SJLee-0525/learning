def backtracking(i, j, N):
    visited[i][j] = 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    if maze[i][j] == 3:
        return 1
    else:
        for k in range(4):
            ni, nj = i + di[k], i + dj[k]
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:
                if backtracking(ni, nj, N):
                    return 1
        return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 미로의 크기
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    stack = []

    for s_i in range(N):
        for s_j in range(N):
            if maze[s_i][s_j] == 2: # 시작 지점
                i, j = s_i, s_j
                break

    visited = [[0] * N for _ in range(N)] # 함수 내에 넣었더니, 재귀 탓인지 깊이 초과 뜸
    print(f'#{tc} {backtracking(i, j, N)}')

