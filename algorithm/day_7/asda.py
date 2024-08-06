T = int(input())

for tc in range(1, T + 1):
    A, B = map(str, input().split())  # A = asakusa  B = sa
    N = len(A)
    M = len(B)
    cnt = 0
    for i in range(N - M + 1):
        temp_i = i
        for j in range(M):
            if A[i+j] != B[j]:
                break
        else:
            cnt += 1
    print(f'#{tc} {N - cnt*(M-1)}')