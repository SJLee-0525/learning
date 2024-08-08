while 1:
    if maze[i][j] == 3:
        return 1
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i + di, j + dj

        if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj]:
            visited[ni][nj] = 1
            stack.append([i, j])
            i, j = ni, nj
            break
    else:
        if stack:
            i, j = stack.pop()
        else:           # 출발점으로 되돌아온 경우
            return 0    # 비정상적 종료


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 미로의 크기
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작 지점 찾기
    for s_i in range(N):
        for s_j in range(N):
            if maze[s_i][s_j] == 2:  # 시작 지점
                start_i, start_j = s_i, s_j

    result = dfs(start_i, start_j)
    print(f"#{tc} {result}")
