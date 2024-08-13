import sys

def f(i, N, K): # 조합 만들기
    if i == N:
        if sum(b) == K:
            temp_chicken = [] # 치킨집으로 만들 수 있는 조합 중 M(K)과 개수가 맞는 경우들을 담음
            for bi in range(N):
                if b[bi]:
                    temp_chicken.append(chicken[bi])
            t_min = 0
            for h in house: # 집들을 순회하며
                temp_min = []
                for c in temp_chicken: # M개의 조합으로 구성된 치킨 집을 돌면서 가장 작은 거리를 더함
                    temp_min.append(abs(c[0] - h[0]) + abs(c[1] - h[1]))
                t_min += min(temp_min)
            min_sum.append(t_min)
    else:
        b[i] = 1
        f(i + 1, N, K)
        b[i] = 0
        f(i + 1, N, K)


N, M = map(int, sys.stdin.readline().split()) # N 도시 크기, M 최대 치킨집 수
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:     # 집 좌표 구하기
            house.append((i, j))
        elif city[i][j] == 2:   # 치킨집 좌표 구하기
            chicken.append((i, j))

b = [0] * len(chicken)
min_sum = []
f(0, len(chicken), M)

print(min(min_sum))

