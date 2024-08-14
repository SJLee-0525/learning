for tc in range(1, 11):
    N = int(input()) # 1 N 아래쪽, 2 S 위쪽으로
    table = [list(map(int, input().split())) for _ in range(N)]
    rotate_table = list(map(list, zip(*table[::-1]))) # 보기 편하게 돌리기
    # print(rotate_table)

    cnt = 0
    for rotate_line in rotate_table:
        judge = True # 앞에 교착되는 게 있는지 판단할 변수 설정
        for elem in rotate_line:
            # 1은 왼쪽으로 가야하고, 2는 오른쪽으로 감
            # 1을 처음 만나도 어차피 바닥에 떨어질거니까 무시
            if elem == 2: # 만약 2를 만나면
                judge = False   # 앞에 2가 있었다는 표시를 남김
            elif elem == 1 and judge == False: # 만약 앞에서 2를 만났다는 증거가 있고, 1을 만났다면
                cnt += 1 # 그 둘은 교착에 빠질것
                judge = True # 다시 true로 전환

    print(f'#{tc} {cnt}')