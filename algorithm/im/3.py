T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    di = [1, 0, -1, 0]          # 델타
    dj = [0, 1, 0, -1]
 
    max_v = 0
    for i in range(N):          # 기준으로 삼을 좌표 설정
        for j in range(N):
            temp = arr[i][j]    # 점수 총합 계산을 위한 임시 변수
            for k in range(4):  # 델타 순회를 위함
                a, b = i, j     # 좌표 값 변경을 위한 재할당
                if 0 <= a + di[k] < N and 0 <= b + dj[k] < N:        # 기준 좌표에서 델타[k]를 더한 좌표가 벗어나지 않는다면
                    while 0 <= a + di[k] < N and 0 <= b + dj[k] < N: # 벗어나지 않는 선에서
                        temp += arr[a + di[k]][b + dj[k]]            # 더함
                        a += di[k]              
                        b += dj[k]                 # 좌표 재설정
            if max_v < temp: # 기존 최대값보다 방금 잰 값이 더 크면 재할당
                max_v = temp
 
    print(f'#{tc} {max_v}')

