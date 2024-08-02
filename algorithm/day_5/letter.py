T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 결과값 담을 변수
    total_count = 0
    for i in range(N):
        count = 0
        for j in range(N):
            # 현재 위치에 1이 있으면 카운트 올림
            if arr[i][j] == 1:
                count += 1
            # 만약 열이 마지막 위치거나, 0인 경우에 count를 확인해봄
            if arr[i][j] == 0 or j == N - 1:
                # count가 K와 일치한다
                if count == K:
                    # 결과 +1
                    total_count += 1
                # 초기화
                count = 0

        # 동시에 세로로도 검사함
        for j in range(N):
            if arr[j][i] == 1:
                count += 1
            if arr[j][i] == 0 or j == N - 1:
                if count == K:
                    total_count += 1
                count = 0

    print(f'#{test_case} {total_count}')