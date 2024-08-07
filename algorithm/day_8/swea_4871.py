def DFS(start, G, V): # start: 출발지점, G: 목표, V: 정점 개수
    visited = [0] * (V + 1) # 방문했는지 여부를 확인할 리스트 생성
    stack = [] # 되돌아갈 경로 확인용 스택
    visited[start] = 1 # 일단 출발점은 방문했잖아
    visit = start # 현재 방문 중인 변수 할당

    yes_no = 0
    while 1:
        for can_go in adjL[visit]: # 일단 방문 중인 정점에서 갈 수 있는 곳이 있다면 꺼내와
            if visited[can_go] == 0: # 꺼내온 애가 방문을 안 했다면
                stack.append(visit) # 나중에 되돌아올 수 있게 현재 위치를 스택에 푸시하고
                visit = can_go # 비짓은 이제 제 겁니다
                visited[visit] = 1 # 방문 도장
                if visit == G: # 만약 가야하는 곳이랑 만났따면
                    yes_no = 1 # 연결됐따는 증거 남김
                break # for can_go: while 1로 되돌아감
        else: # 만약 visit에서 갈 수 있는 정점이 없었다면
            if len(stack) > 0:  # if stack 대용으로 가능? 스택에 자료가 하나라도 있다면
                visit = stack.pop() # 가장 마지막 위치로 되돌아감
            else: # 만약 되돌아갈 곳도 없어
                return yes_no
    pass



T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split()) # V 정점 개수, E 간선 개수
    adjL = [[] for _ in range(V + 1)] # 연결 경로를 담을 2차원 리스트 생성

    for _ in range(E):
        n_start, n_end = map(int, input().split())
        adjL[n_start].append(n_end)  # 출발 번호를 인덱스로, 값을 연결된 경로로 하는 리스트 만들기

    # print(adjL) # [[], [4, 3], [3, 5], [], [6], [], []]
    S, G = map(int, input().split()) # 출발 노드 S / 도착 노드 G

    print(f'#{tc} {DFS(S, G, V)}')

