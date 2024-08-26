T = int(input()) # 테스트 케이스 수

for tc in range(1, T + 1):
    N, K = map(int, input().split()) # 활동구역 수, 이동할 수 있는 최대 거리
    arr = list(map(int, input().split())) # 활동구역 정보

    full = K # 현재 포만도
    for n in range(N): # 배열을 순회
        if arr[n]: # 만약 먹이가 있으면 배를 채움
            full = K
        elif full == 0: # 공복 상태가 되면 결과 값 갱신하고 종료
            result = n
            break
        full -= 1 # 이동할 때마다 포만도 감소
        result = n # 이동할 때마다 결과 값 갱신

    if K == 0: # 만약 K가 0이면 1칸도 못 감
        result = 0

    print(f'#{tc} {result + 1}') # 칸의 값은 실제 인덱스 값보다 1 많음