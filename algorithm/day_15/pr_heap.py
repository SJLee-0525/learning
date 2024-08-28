def enQ(num):
    global last
    last += 1
    H[last] = num
    c = last
    p = c // 2
    while p >= 1 and H[p] > H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c // 2
    # print(H)

def cnt(N):
    p = N // 2
    c = 0
    while p >= 1:
        c += H[p]
        p //= 2
    return c


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    H = [0] * (N + 1)
    last = 0

    for a in arr:
        enQ(a)

    print(f'#{tc} {cnt(N)}')
