T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 당근밭 구역의 수
    district = list(map(int, input().split()))

    min_gap = 200           # 구역은 최대 20개, 당근은 10개 이하
    min_index = 0
    for i in range(1, N):   # 경계 지정: N = 5 기준 1 ~ 4
        A = 0               # A가 해당 경계 범위에서 수확하는 양 계산
        for i_a in range(i):
            A += district[i_a]
        
        B = 0               # B가 해당 경계 범위 기준으로 수확하는 양 계산
        for i_b in range(i, N):
            B += district[i_b]
        
        temp_gap = A - B        # 둘의 차 계산
        if temp_gap < 0:        # 만약 음수면 양수로 변환
            temp_gap *= -1

        if min_gap > temp_gap:  # 최소값 비교 후, 인덱스까지 따라 저장
            min_gap = temp_gap
            min_index = i

    print(f'#{tc} {min_index} {min_gap}')    
