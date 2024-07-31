T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # N은 격자판의 c, M은 r
    bl_arr = [list(map(int, input().split())) for _ in range(N)]

    # 순회할 때 쓸 값 설정
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    max_Pollen = 0
    # 기준점 설정
    for i in range(N):
        for j in range(M):
            Pollen = bl_arr[i][j]

            # di, dj를 사용해 상하좌우 탐색토록
            for k in range(4):
                mi = i + di[k]
                mj = j + dj[k]
                # index Error가 나지 않는 선에서
                if 0 <= mi < N and 0 <= mj < M:
                    Pollen += bl_arr[mi][mj]
            if max_Pollen < Pollen:
                max_Pollen = Pollen

    print(f'#{test_case} {max_Pollen}')

