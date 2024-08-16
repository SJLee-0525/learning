T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
 
    judge = True
    for i in range(9):
        garo_sum = 0
        sero_sum = 0
        for j in range(9):
            garo_sum += arr[i][j]
            sero_sum += arr[j][i]
            if i % 3 == 0 and j % 3 == 0: # 3칸씩 묶어서 검증할 부분
                nemo_sum = 0
                for i2 in range(i, i + 3):
                    for j2 in range(j, j + 3):
                        nemo_sum += arr[i2][j2]
                if nemo_sum != 45:
                    judge = False
                    break
        if garo_sum != 45 or sero_sum != 45:
            judge = False
            break
 
    if judge == True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')