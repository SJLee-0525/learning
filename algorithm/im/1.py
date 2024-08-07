T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N 세로, M 가로
    pic = [list(map(int, input().split())) for _ in range(N)]
    
    max_len = 0         # 최대값 비교를 위한 변수 설정
    for i in range(N):  # 행으로 끊어 탐색
        j = 0           # 인덱스 수동 설정
        while j < M:
            if pic[i][j] == 1:  # 만약 인덱스가 가리키는 값이 1이면
                str_len = 0     # 임시 길이 변수 할당
                while j < M and pic[i][j] == 1: # 인덱스를 벗어나지 않고 1을 가리키는 조건 하에서
                    j += 1          # 인덱스 추가하고
                    str_len += 1    # 길이도 추가
                if str_len >= 2:    # 루프를 다 돌고 나왔을 때 길이가 2 이상이면
                    if max_len < str_len: # 최대값 비교
                        max_len = str_len
            j += 1
    
    for j2 in range(M): # 열로 끊어 탐색, 위와 같음
        i2 = 0
        while i2 < N:
            if pic[i2][j2] == 1:
                str_len_2 = 0
                while i2 < N and pic[i2][j2] == 1:
                    i2 += 1
                    str_len_2 += 1
                if str_len_2 >= 2:
                    if max_len < str_len_2:
                        max_len = str_len_2
            i2 += 1
    
    print(f'#{tc} {max_len}')
    
    # for i in range(N):
    #     for j in range(M):
    #         if i < j:
    #             pic[i][j], pic[j][i] = pic[j][i], pic[i][j]
    

            