def find_square(N, arr):
    global judge
    # 돌다가 # 발견하면 그걸 시작점으로 check 함수 호출
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "#":
                check(i, j, N, arr)
                return
    # 만약 못 찾으면 False로 바꾸고 다음 함수 호출 없이 종료
    # 테케 중에 아무 것도 없는 게 있음... 여기서 계속 실패함................
    else:
        judge = False
        return

def check(i, j, N, arr):
    bi = i
    # 한 쪽 면 길이 구하기
    # 어차피 정사각형 구하는거니까 한 쪽 면 길이만 구하고,
    # 세로로도 돌면서 그 안에 있는지만 확인하면 그만
    while 0 <= bi < N and arr[bi][j] == '#':
        bi += 1
    L = bi - i # 발견한 사각형의 순수 세로 길이

    # #이 있었던 시작점부터 정사각형 길이의 해당 범위만큼만 돌아서 #을 지움
    for ci in range(i, i + L):
        for cj in range(j, j + L):
            if 0 <= ci < N and 0 <= cj < N:
                if arr[ci][cj] != '#':
                    # 만약 #이 아닌 게 있다면 걍 종료
                    return
                elif arr[ci][cj] == '#':
                    # '#'이 있다면 .으로 바꿈
                    arr[ci][cj] = '.'
    else:
        # 문제 없이 다 돌면 확인 함수 호출
        final_check(N, arr)

def final_check(N, arr):
    global judge
    cnt = 0
    # 돌면서 #이 남아있으면 #이 다 안 지워진 것: 정사각형이 아님
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                cnt += 1
    if cnt == 0:
        # 하나도 없었다면 정사각형 하나 있던 것
        judge = True
    return

####################################################

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 판단 변수
    judge = False
    find_square(N, arr)
    # print(arr)

    if judge == True:
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')