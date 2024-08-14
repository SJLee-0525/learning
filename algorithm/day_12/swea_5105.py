from collections import deque

def find_start(N, maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def BFS(si, sj, N):
    global visited
    Q = deque()         # 큐 생성
    Q.append((si, sj))  # 큐에 위치 삽입
    visited[si][sj] = 1 # 방문 표시

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]  # 탐색용 델타

    while Q:                # 큐에 자료가 있는 동안
        i, j = Q.popleft()  # 큐에서 자료를 입력한 순으로 뽑아옴
        if maze[i][j] == 3: # 만약 뽑아온 위치가 도착지라면
            return visited[i][j] - 2 # visited에 할당된 값을 리턴
        for k in range(4):
            mi, mj = i + di[k], j + dj[k]
            if 0 <= mi < N and 0 <= mj < N and maze[mi][mj] != 1 and visited[mi][mj]== 0:
                # 이동하는 위치가 인덱스 범위를 벗어나지 않고, 벽이 아니고 방문한 적이 없다면
                Q.append((mi, mj))  # 큐에 담음
                visited[mi][mj] = visited[i][j] + 1 # 기존에 할당된 것에 추가로 더해서 경로 거리 계산
    return 0 # 비정상 종료

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 미로 크기
    maze = [list(map(int, input())) for _ in range(N)]

    si, sj = find_start(N, maze)

    visited = [[0] * N for _ in range(N)]
    print(f'#{tc} {BFS(si, sj, N)}')
