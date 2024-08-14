import pprint
def change(y, x, color, N):
    global board
    dx = [1, 0, -1, 0, 1, 1, -1, -1] # 델타
    dy = [0, 1, 0, -1, -1, 1, 1, -1]

    judge = False
    for k in range(8): # 델타 순회
        my, mx = y + dy[k], x + dx[k]
        if 0 <= my < N and 0 <= mx < N and board[my][mx] != 0 and board[my][mx] != color:
            # 만약 주변 돌이 다른 돌이면 탐색 시작
            while 0 <= my < N and 0 <= mx < N and board[my][mx] != 0 and board[my][mx] != color:
                # 같은 조건 하에서 계속 범위를 넓혀가다가
                my += dy[k]
                mx += dx[k]
                if 0 <= my < N and 0 <= mx < N and board[my][mx] == color:
                    judge = True
                    # 만약 가다가 결국 내 돌을 만나면 그 사이에 있는 돌을 뒤집을 수 있음
                    my += -(dy[k])
                    mx += -(dx[k])
                    # 온 길을 되돌아가면서 뒤집음
                    while 1:
                        board[my][mx] = color
                        my += dy[k] * -1
                        mx += dx[k] * -1
                        # 만약 시작위치로 오면 다음 탐색
                        if y == my and x == mx:
                            break

        # 다 돌고 바꾼게 있었다면 원래 위치에 돌도 놔줌
        if k == 7 and judge == True:
            board[y][x] = color
            return
    return

#############################

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 보드 길이 / 놓는 횟수
    # (좌표) 1 흑돌, 2 백돌
    board = [[0] * N for _ in range(N)]

    # 기본 돌 배치
    for si in range(N//2 - 1, N//2 + 1):
        for sj in range(N//2 - 1, N//2 + 1):
            if si == sj:
                board[si][sj] += 2
            else:
                board[si][sj] += 1

    # 명령을 받아 수행
    for _ in range(M):
        y, x, color = map(int, input().split())
        y, x = y - 1, x - 1
        change(y, x, color, N)

    # 카운트
    B = 0
    W = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                B += 1
            elif board[i][j] == 2:
                W += 1
    print(f'#{tc} {B} {W}')