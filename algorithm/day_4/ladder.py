for test_case in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for start in range(100):
        if arr[0][start] == 1:
            i, j = 0, start
            while i < 99:
                if j > 0 and arr[i][j - 1] == 1:
                    while j > 0 and arr[i][j - 1] == 1:
                        j -= 1
                elif j < 99 and arr[i][j + 1] == 1:
                    while j < 99 and arr[i][j + 1] == 1:
                        j += 1
                i += 1

            if i == 99 and arr[i][j] == 2:
                print(f'#{test_case} {start}')
                break