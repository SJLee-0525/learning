# 기지국 범위 정보
d = {'A': 1, 'B': 2, 'C': 3}

def find_base(N):
    '''기지국 찾기'''
    for i in range(N):
        for j in range(N):
            if arr[i][j] in d: # 만약 해당 좌표 데이터가 기지국이면 함수 호출
                check(i, j, arr[i][j])

def check(i, j, type):
    '''기지국이 커버하는 범위 내의 집들을 변환시키는 함수'''
    global arr
    type_num = d[type] # d 딕셔너리 내의 기지국 value 할당

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for k in range(4):
        for l in range(1, type_num + 1):
            mi, mj = i + (di[k] * l), j + (dj[k] * l) # 기지국 커버 범위만큼 더
            if 0 <= mi < N and 0 <= mj < N:
                if arr[mi][mj] == 'H':
                    arr[mi][mj] = 'D' # 중복 예방

def ctt(N):
    '''마지막 카운팅'''
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H': # 만약 집이면 카운트 + 1
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    find_base(N)

    print(f'#{tc} {ctt(N)}')
