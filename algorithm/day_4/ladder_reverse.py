for test_case in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for end in range(100):
        if arr[99][end] == 2:
            i, j = 99, end
            while i > 0:
                if j > 0 and arr[i][j - 1] == 1:
                    while j > 0 and arr[i][j - 1] == 1:
                        j -= 1
                elif j < 99 and arr[i][j + 1] == 1:
                    while j < 99 and arr[i][j + 1] == 1:
                        j += 1
                i -= 1
            if i == 0:
                print(f'#{test_case} {j}')

