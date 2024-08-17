def square(si, sj, N):
    di, dj = si, sj

    # 1이 나오는 동안 가로 세로 확장
    while di < N and arr[di][sj] == 1:
        di += 1
    while dj < N and arr[si][dj] == 1:
        dj += 1

    # 추후 혼선 방지를 위해서 체크한 범위는 0으로 변환
    for ti in range(si, di):
        for tj in range(sj, sj):
            arr[ti][tj] = 0

    # 직사각형 넓이 반환
    return (di - si) * (dj - sj)

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 배열 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    rst = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1: # 사각형 부분 발견하면 함수 호출
                tmp_rst = square(i, j, N)
                if rst < tmp_rst:
                    rst = tmp_rst

    print(f'#{tc} {rst}')