T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N개의 줄에 M개씩
    pic = [list(map(int, input().split())) for _ in range(N)]

    max_data = 0
    for i in range(N):
        cnt_garo = 0
        cnt_sero = 0
        for j in range(M):
            # 가로 연산
            if pic[i][j] == 1:
                cnt_garo += 1
            if pic[i][j] == 0:
                if cnt_garo <= 1:
                    cnt_garo = 0
                else:
                    if max_data < cnt_garo:
                        max_data = cnt_garo
                    cnt_garo = 0
        if cnt_garo > 1:
            if max_data < cnt_garo:
                max_data = cnt_garo

    for jj in range(M):
        for ii in range(N):
            # 세로 연산
            if pic[ii][jj] == 1:
                cnt_sero += 1
            if pic[ii][jj] == 0:
                if cnt_sero <= 1:
                    cnt_sero = 0
                else:
                    if max_data < cnt_sero:
                        max_data = cnt_sero
                    cnt_sero = 0
        if cnt_sero > 1:
            if max_data < cnt_sero:
                max_data = cnt_sero

    print(f'#{tc} {max_data}')