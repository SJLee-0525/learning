from collections import deque

def BFS(S, G):
    global visited  # visited를 함수 내에 만들지 말아보자
    Q = deque()     # 큐 생성
    visited[S] = 1  # 방문 표시
    Q.append(S)     # 큐에 방문한 곳 삽입 (준비)
    while Q:        # 큐에 자료가 있는 동안
        t = Q.popleft() # 큐에서 노드를 가져옴
        if t == G:      # 만약 가져온 노드가 목표 노드라면
            # print(visited)
            return visited[t] - 1 # 종료 # - 1 해줘야 지난 간선의 수가 나오는 듯
        for w in adjL[t]:   # 가져온 노드에서 갈 수 있는 곳들을 탐색
            if visited[w] == 0: # 탐색한 노드가 가보지 않은 곳이라면
                Q.append(w)     # 큐에 넣고
                visited[w] = visited[t] + 1 # visited에 표시 (기존 것에 1을 더함으로 경로 거리로 표시)
    return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())    # 노드개수 V, 간선 수 E
    adjL = [[] for _ in range(V + 1)]   # 인접한 노드를 나타내는 리스트 생성
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adjL[v1].append(v2)
        adjL[v2].append(v1)

    visited = [0] * (V + 1) # visited 변수 생성
    S, G = map(int, input().split()) # start, go
    # print(adjL)
    print(f'#{tc} {BFS(S, G)}')