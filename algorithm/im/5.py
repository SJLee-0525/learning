T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N 행 M 열
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0, -1, 0]  # 델타
    dj = [0, 1, 0, -1]

    max_score = 0       # 최대값 비교를 위한 변수
    for i in range(N):
        for j in range(M):
            temp_sum = arr[i][j]    # 기준점 잡고, 합계 계산을 위한 변수에 할당
            temp = temp_sum         # 추가 순회를 위한 변수
            for k in range(4):  # 델타 순회
                for n in range(1, temp + 1): # arr[i][j]의 값만큼 터지므로 범위 설정
                    if 0 <= i + (di[k] * n) < N and 0 <= j + (dj[k] * n) < M:   # 인덱스 범위가 벗어나지 않으면
                        temp_sum += arr[i + (di[k] * n)][j + (dj[k] * n)]           # 연산
            if max_score < temp_sum:    # 최대값 비교
                max_score = temp_sum
    
    print(f'#{tc} {max_score}')