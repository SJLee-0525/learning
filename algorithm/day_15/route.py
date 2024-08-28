from collections import deque

def find_summit_height(N):
    '''가장 높은 봉우리 찾기'''
    temp = 0
    for i in range(N):
        for j in range(N):
            if temp < arr[i][j]:
                temp = arr[i][j]
    return temp

def find_coord(N, K, summit, arr):
    '''탐색하다 가장 높은 봉우리 나오면 탐색 하도록'''
    for i in range(N):
        for j in range(N):
            if arr[i][j] == summit: # 가장 높은 봉우리 등장
                cal_route(i, j, K, arr) # 탐색

def cal_route(i, j, K, arr, s=0, constructed=False, visited=None):
    # cal_route(좌표, 깎을 수 있는 크기, 지도, 등산로 길이, 건설 여부, visited)
    global longest
    if visited == None: # visited가 없다면
        visited = [[0] * N for _ in range(N)] # visited 생성

    if longest < s + 1: # 등산로 길이가 현재 최대 값보다 높다면
        longest = s + 1 # 갱신

    visited[i][j] = 1   # 방문 표시

    for k in range(4):  # 델타 탐색
        mi, mj = i + di[k], j + dj[k]
        if 0 <= mi < N and 0 <= mj < N and visited[mi][mj] == 0: # 방문한 적이 없고, 범위를 벗어나지 않는데
            if arr[i][j] > arr[mi][mj]: # 갈 곳의 높이가 현재 위치보다 낮다면
                cal_route(mi, mj, K, arr, s + 1, constructed, visited)
                # 위치 새로 주고, 기존 지도 전달, 거리는 1 늘리고, 기존 건설여부, 만들어진 visited 전달해서 재귀
            elif constructed == False and arr[i][j] + K > arr[mi][mj]:
                # 만약 건설한 적이 없는데, 건설해서 갈 수 있는 높이라면
                new_arr = [a[:] for a in arr]   # 맵 새로 생성 (2차원 리스트 복사)
                new_arr[mi][mj] = arr[i][j] - 1 # 해당 위치를 현재 위치 높이보다 1 낮게 만들어 주고
                cal_route(mi, mj, K, new_arr, s + 1, True, visited)
                # 위치 새로 주고, 거리는 1 늘리고, 새로운 맵 전달, 거리는 1 늘리고, 건설 여부 True로 변경, visited 전달해서 재귀

    visited[i][j] = 0
    # 다 탐색하면 현재 위치의 visited를 0으로 만들어 다른 곳에서 탐색올 수 있도록 변경

###################################################################

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 4방향 델타
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    longest = 0

    summit = find_summit_height(N)  # 가장 높은 봉우리 높이 찾기
    find_coord(N, K, summit, arr)   # 높은 봉우리를 찾아서 탐색

    print(f'#{tc} {longest}')