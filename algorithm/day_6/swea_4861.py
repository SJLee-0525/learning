T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N 배열 크기 / M 회문 길이
    arr = [list(input()) for _ in range(N)]

    for i in range(N): # 인덱스 범위를 넘기지 않기 위해 기준 축 조정
        for j in range(N - M + 1):
            # 가로 검사: 기준 범위에서 M 만큼의 범위를 가진 k를 이용해 회문 검사
            for k in range(M // 2):
                if arr[i][j + k] != arr[i][j + M - k - 1]:
                    break
            else: # 만약 문제 없이 잘 돌았다면 출력
                print(f'#{tc} ', end='')
                for k2 in range(M):
                    print(arr[i][j + k2], end='')
                print()

            # 세로 검사: 기준 범위에서 M 만큼의 범위를 가진 k를 이용해 회문 검사
            for k3 in range(M // 2):
                if arr[j + k3][i] != arr[j + M - k3 - 1][i]:
                    break
            else: # 만약 문제 없이 잘 돌았다면 출력
                print(f'#{tc} ', end='')
                for k4 in range(M):
                    print(arr[j + k4][i], end='')
                print()

