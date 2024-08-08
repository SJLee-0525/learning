# stack
def find_start(N):  # '2'인 칸 리턴
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':  # 미로를 string으로 저장한 경우
                return i, j
    return -1, -1  # 조건문 안의 return에 대한 디버깅 용도


def dfs(i, j, N):
    stack = []  # 스택 생성, visited는 외부에서 생성 (내부에서 선언해도 무관)
    visited[i][j] = 1  # 시작점 방문 표시
    while True:  # 인접 칸으로 갈 수 있으면 경로를 저장하고 이동하는 방식
        if maze[i][j] == '3':
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # i, j에 인접한 ni, nj 중 이동 가능한 지점
            ni, nj = i + di, j + dj
            # 벽으로 둘러지지 않은 미로, 벽이 아닌 칸
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != '1' and visited[ni][nj] == 0:
                visited[ni][nj] = 1  # v에 인접하고 미방문인 w(=maze[ni][nj])가 있으면
                stack.append([i, j])  # 스택에 경로(= 현재 위치)를 저장하고
                i, j = ni, nj  # w로 이동, v <- w
                break  # 이동 완료
        else:  # 이동할 수 있는 칸이 없으면
            if stack:  # 지나온 칸이 남아 있으면
                i, j = stack.pop()  # 그 칸에서 다른 방향을 탐색

            else:  # 스택이 빈 경우 (= 출발점으로 되돌아온 경우)
                return 0
    return -1  # 비정상 탐색 종료


T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 미로의 가로세로 크기
    maze = [input() for _ in range(N)]  # 미로 자체는 수정 X, visitied[][] 사용
    visited = [[0] * N for _ in range(N)]  # 방문한 칸 표시
    sti, stj = find_start(N)
    result = dfs(sti, stj, N)
    print(f'#{tc} {result}')