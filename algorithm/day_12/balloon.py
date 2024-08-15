T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    max_fanfare = 0
    for i in range(N):
        for j in range(M):
            fanfare = balloons[i][j]
            temp_fanfare = balloons[i][j]
            for k in range(4): # 델타 순회
                for k2 in range(1, fanfare + 1): # 처음 터진 팡파레의 수 만큼
                    mi, mj = i + (di[k] * k2), j + (dj[k] * k2)
                    if 0 <= mi < N and 0 <= mj < M:
                        temp_fanfare += balloons[mi][mj]
            if max_fanfare < temp_fanfare:
                max_fanfare = temp_fanfare
    
    print(f'#{tc} {max_fanfare}')