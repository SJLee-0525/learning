def dfs(i, j):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    stack = []              # 돌아갈 길 담을 스택
    stack.append((i, j))    # 현 위치 담음

    while stack:            # 스택에 자료가 있는 동안
        if maze[i][j] == 3: # 출구를 찾으면
            return 1
        maze[i][j] = 5  # 흔적 남기기
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and (maze[ni][nj] == 0 or maze[ni][nj] == 3):
                stack.append((ni, nj))
        i, j = stack.pop() # 최후의 보루
    return 0  # 출구를 찾지 못함

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
