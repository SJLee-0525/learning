def DFS(adjL):          # 시작점은 0, 목표는 99라서 굳이 매개변수 넣을 필요 업므
    visited = [0] * 100 # 방문했는지 확인용
    stack = []          # 되돌아갈 스택
    visit = 0           # 시작점
    visited[visit] = 1  # 흔적 남기기

    while 1:
        for w in adjL[visit]:       # 내 위치에서 갈 수 있는 곳들 뽑아모 [[1, 2], [4, 3], [9, 5], [7], [8, 3], [6, 7], [10], [99, 9], [], [8, 10], [],...
            if visited[w] == 0:     # 그 중 안 방문 한 곳에 한해서
                stack.append(visit) # 일단 돌아갈 수 있도록 현 위치 푸시
                visit = w           # 위치 바꿈
                visited[visit] = 1  # 재할당
                if visit == 99:     # 만약 99면
                    return 1        # 와 신난다
                break
        else:                       # 위에서 문제 없이 돌거나, 들어가지 ㅗㅁㅅ하면
            if stack:               # 스택에 자료가 있다면
                visit = stack.pop() # 내 위치는 상위 디렉토리로
            else:                   # 만약에 갈 곳이 없다면
                return 0            # 난 갈 곳이 업서

for _ in range(1, 11):
    tc, road = map(int, input().split())
    arr = list(map(int, input().split()))
    adjL = [[] for _ in range(100)] # 0 ~ 99

    for i in range(road):
        v1, v2 = arr[i * 2], arr[i * 2 + 1] # 한번에 할라 했는데 안 됐음.. 나눠 ㅎ하자
        # print(v1,v2)
        adjL[v1].append(v2)
    # print(adjL)

    print(f'#{tc} {DFS(adjL)}')