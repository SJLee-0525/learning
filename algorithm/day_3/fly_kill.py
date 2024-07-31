T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # N은 배열의 너비, M은 파리채의 너비
    fly_arr = [list(map(int, input().split())) for _ in range(N)] # 배열 생성

    max_kill_count = 0
    # 인덱스 에러가 나지 않도록 파리채 크기에 맞춰 기본 탐색 인덱스를 조정
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 한 인덱스의 기준에서 잡을 수 있는 파리의 수 구하기
            kill_count = 0
            # 현재 위치에서 파리채 크기만큼 더한 인덱스 범위 탐색 후 죽인 수 추가
            for kill_i in range(i, i + M):
                for kill_j in range(j, j + M):
                    kill_count += fly_arr[kill_i][kill_j]
            # 최대값 조정
            if max_kill_count < kill_count:
                max_kill_count = kill_count

    print(f'#{test_case} {max_kill_count}')

