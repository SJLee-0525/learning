from collections import deque

def find_start():
    for i in range(1, V + 1):
        if can_do[i] == 0:
            start.append(i)


def bfs(st_list):
    Q = deque(st_list)
    visited = [0] * (V + 1)
    for s in st_list:
        visited[s] = 1

    while Q:
        now = Q.popleft()
        result.append(now)
        for w in adjL[now]:
            can_do[w] -= 1
            if can_do[w] == 0 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[now] + 1

######################################################################

for tc in range(1, 11):
    V, E = map(int, input().split()) # 정점의 개수, 간선의 개수
    arr = list(map(int, input().split()))

    adjL = [[] for _ in range(V + 1)]
    can_do = [0] * (V + 1)
    for i in range(E):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        adjL[v1].append(v2)
        can_do[v2] += 1

    start = []
    find_start()

    result = []
    bfs(start)

    print(f'#{tc}', *result)
