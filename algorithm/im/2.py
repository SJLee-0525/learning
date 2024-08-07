T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N 돌 상태, M 뒤집기 횟수
    stones = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split()) # ㅑ 기준점, j 범위
        i -= 1  # 인덱스와 맞추기 위함
        k = 1   # 인덱스 조정을 위한 변수 할당
        while 0 <= i - k and i + k < N and k <= j:         # 인덱스 범위를 벗어나지 않는 선에서
            if stones[i - k] == stones[i + k]:  # 마주보는 두 돌의 값이 같을 경우에
                if stones[i - k] == 0:          # 원래의 값을 뒤집음
                    stones[i - k] = stones[i + k] = 1
                else:
                    stones[i - k] = stones[i + k] = 0
            k += 1                              # 더 넓은 범위 탐색을 위한 변수 조정
    
    print(f'#{tc}', *stones)

