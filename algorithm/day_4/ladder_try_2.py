for test_case in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    di = [1, 0, 0]
    dj = [0, 1, -1]

    for start in range(100):
        if arr[0][start] == 1:
            i, j = 0, start
            while i < 99:
                if 0 < j and arr[i][j - 1] == 1:
                    k = 2
                    while 0 < j and arr[i][j + dj[k]] == 1:
                        i += di[k]
                        j += dj[k]
                elif j < 99 and arr[i][j + 1] == 1:
                    k = 1
                    while j < 99 and arr[i][j + dj[k]] == 1:
                        i += di[k]
                        j += dj[k]  
                k = 0                      
                i += di[k]
                j += dj[k]

            if arr[i][j] == 2:
                print(f'#{test_case} {start}')