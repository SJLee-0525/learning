'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def BFS(s, V): # 시작점, 정점 수
    visited = [0] * (V + 1) # visited 생성
    queue = []              # 큐 생성
    queue.append(s)         # 시작점 enqueue
    visited[s] = 1          # 시작점 방문 표시
    while queue:            # queue에 자료가 있는 동안 (탐색할 정점이 남아있으면)
        t = queue.pop(0)    # t를 dequeue
        print(t, end=' ')   # visit(t) # 할 작업
        for w in adjL[t]:   # 뽑은 t에 연결된 곳이 있는지 확인
            if visited[w] == 0: # 만약 뽑은 것이 방문된 적이 없는 곳이라면 (queue에 들어간 적이 없다면)
                queue.append(w) # queue에 enQueue
                visited[w] = visited[t] + 1  # enQueue 된 적이 있음을 표시 (간선을 몇 개 거쳤는지: 최단거리)
    print()
    print(visited)


# 마지막 정점번호, 간선 수
V, E = map(int, input().split())
adjL = [[] for _ in range(V + 1)]
input_arr = list(map(int, input().split()))
for e in range(E):
    v1, v2 = input_arr[e * 2], input_arr[e * 2 + 1]
    adjL[v1].append(v2)
    adjL[v2].append(v1) # 무향일 때는 여기까지 추가시켜줘야함


BFS(1, V) # 1번부터 시작을 하고, 마지막 정점을 알려줌 (출발점, 정점 수)
BFS(2, V)
BFS(7, V)
