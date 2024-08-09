def f(i, N):
    if i == N:
        for j in range(N):
            if b[j]:
                print(arr[j], end=' ')
        print()
    else:
        b[i] = 1
        f(i + 1, N)
        b[i] = 0
        f(i + 1, N)

def f2(i, N, K):
    global cnt
    if i == K:
        cnt += 1
        print(arr)
    for j in range(i, N):
        arr[i], arr[j] = arr[j], arr[i]
        f2(i + 1, N, K)
        arr[i], arr[j] = arr[j], arr[i]

arr = [1, 2, 3, 4, 5]
N = 5
K = 3
b = [0] * N
cnt = 0
# f(0, N)
f2(0, N, K)
print(cnt)