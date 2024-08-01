T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    i, j, k = 0, -1, 0    

    for num in range(1, N * N + 1):
        if 0 <= i + di[k] < N and 0 <= j + dj[k] < N and arr[i + di[k]][j + dj[k]] == 0:
            arr[i + di[k]][j + dj[k]] = num
            i += di[k]
            j += dj[k]
            print(i, j)
        else:
            k += 1
            if k == 4:
                k = 0
            arr[i + di[k]][j + dj[k]] = num
            i += di[k]
            j += dj[k]            

        print(arr)
