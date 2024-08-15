T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 영역 크기, 파리채 크기
    ground = [list(map(int, input().split())) for _ in range(N)]

    max_kill_count = 0
    # 파리채 고려해서 기준점 인덱스 크기 조정
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            kill_count = 0
            # 기준점을 기준으로 파리채 범위만큼
            for i2 in range(i, i + M):
                for j2 in range(j, j + M):
                    kill_count += ground[i2][j2]
            if max_kill_count < kill_count:
                max_kill_count = kill_count

    print(f'#{tc} {max_kill_count}')