def f(i, N, M):  # i번째 교환, M 자릿수
    global max_v
    if i == N:
        d = 0  # num을 십진수로 만들어서 최대 상금과 비교하기
        for x in num:
            d = d * 10 + x
        if max_v < d:
            max_v = d
    else:
        for p in range(M - 1):  # 두 개를 고르는 조합
            for q in range(p + 1, M):
                num[p], num[q] = num[q], num[p]
                d = 0  # num을 십진수로 만들어서 i교환횟수에 이미 만들어 진적이 있는지 확인
                for x in num:
                    d = d * 10 + x
                if v[d] & (1 << i) == 0:
                    v[d] |= 1 << i
                    # if v[d][i] == 0:
                    #     v[d][i] = 1
                    f(i + 1, N, M)
                num[p], num[q] = num[q], num[p]


T = int(input())
for tc in range(1, T + 1):
    num, N = input().split()  # 123 1
    num = list(map(int, num))  # [1,2,3]
    N = int(N)  # 1
    # v = [[0]*N for _ in range(1000000)] # 메모리 초과
    v = [0] * 1000000

    max_v = 0
    M = len(num)
    f(0, N, M)
    print(f'#{tc} {max_v}')