
# 리스트 사용
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    station = [0] * 5001
    for line in range(N):
        start, end = map(int, input().split())
        for i in range(start, end + 1):
            station[i] += 1
        
    P = int(input())
    print(f'#{test_case} ', end='')
    for check in range(P):
        print(station[int(input())], end = ' ')
    print()