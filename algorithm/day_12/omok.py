T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    judge = False # 출력때 사용할 판단 변수 설정

    # 일반적인 가로 세로 순회하며 연속적인으로 배치된 알 확인
    for i in range(N):
        garo = 0
        sero = 0
        for j in range(N):
            # 가로
            if arr[i][j] == 'o':
                garo += 1
                if garo >= 5:
                    judge = True
            if arr[i][j] == '.':
                garo = 0

            # 세로
            if arr[j][i] == 'o':
                sero += 1
                if sero >= 5:
                    judge = True
            if arr[j][i] == '.':
                sero = 0

    # 11-5 방향으로 대각선 오목 여부 확인 (아래와 같은 방식으로 인덱스 출력됨)
    '''
    0 0
    0 1
    0 2
    0 3
    0 4

    1 1
    1 2
    1 3
    1 4

    2 2
    2 3
    2 4

    3 3
    3 4
    
    4 4
    '''
    for ii in range(N):
        cross_1a = 0
        cross_1b = 0
        for jj in range(N - ii):
            # print(jj, ii + jj)
            if arr[jj][ii + jj] == 'o':
                cross_1a += 1
                if cross_1a >= 5:
                    judge = True
            if arr[jj][ii + jj] == '.':
                cross_1a = 0

            if arr[ii + jj][jj] == 'o':
                cross_1b += 1
                if cross_1b >= 5:
                    judge = True
            if arr[ii + jj][jj] == '.':
                cross_1b = 0

    # 1-7 방향으로 대각선 오목 여부 확인
    '''
    0 0

    0 1
    1 0

    0 2
    1 1
    2 0

    0 3
    1 2
    2 1
    3 0

    0 4
    1 3
    2 2
    3 1
    4 0

    1 4
    2 3
    3 2
    4 1

    2 4
    3 3
    4 2

    3 4
    4 3

    4 4
    '''
    for st in range((N - 1) * 2 + 1):
        cross_2 = 0
        for iii in range(N):
            for jjj in range(N):
                if iii + jjj == st:
                    # print(iii,jjj)
                    if arr[iii][jjj] == 'o':
                        cross_2 += 1
                        if cross_2 >= 5:
                            judge = True
                    elif arr[iii][jjj] == '.':
                        cross_2 = 0

    # 판단 변수에 따라서 출력 다르게
    if judge == True:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')