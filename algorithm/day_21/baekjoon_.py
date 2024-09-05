from collections import deque
import sys
import pprint
import copy

def check():
    for f in range(H):
        for i in range(M):
            for j in range(N):
                if box[f][i][j] == 0:
                    return False
    else:
        return True

def std(floor, i_box, n_box=None):
    # print(floor, i_box)
    if n_box == None:
        n_box = [[[0] * N for _ in range(M)] for __ in range(H)]
    if floor == H:
        # print('f', n_box)
        return n_box

    # 해당 층의 익어있는 토마토 좌표들을 삽입
    Q = deque()
    for i in range(M):
        for j in range(N):
            if i_box[floor][i][j] == 1:
                n_box[floor][i][j] = 1
                Q.append((i, j))
            elif i_box[floor][i][j] == -1:
                n_box[floor][i][j] = -1

    # 해당 층에서 상하좌우 범위만큼 익혀줌
    # print(floor, Q)
    while Q:
        i, j = Q.popleft()
        for k in range(4):
            mi, mj = i + di[k], j + dj[k]
            if 0 <= mi < M and 0 <= mj < N and i_box[floor][mi][mj] == 0:
                n_box[floor][mi][mj] = 1
    # print('n', n_box)

    # 윗층과 아래층을 비교해서 상하로 영향 받는 토마토 확인 후 반영
    for t_floor in range(H - 1, H + 2):
        if 0 <= t_floor < H:
            for ti in range(M):
                for tj in range(N):
                    if i_box[t_floor][ti][tj] == 1 and n_box[floor][ti][tj] == 0:
                        n_box[floor][ti][tj] = 1

    std(floor + 1, i_box, n_box)
    return n_box


N, M, H = map(int, sys.stdin.readline().split())
# N 가로, M 세로, H 높이

box = [[list(map(int, sys.stdin.readline().split())) for _ in range(M)] for _ in range(H)]
# pprint.pprint(box)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

day = 0
while 1:
    temp = std(0, box)
    # print('temp', temp)
    if temp == box:
        if not check():
            day = -1
        break
    else:
        day += 1
        box = copy.deepcopy(temp)

print(day)