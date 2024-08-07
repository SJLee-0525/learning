T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N 구역 개수, M 수레 용량
    arr = [0] + list(map(int, input().split()))

    i = 1                   # 인덱스 지정
    cnt = 0                 # 왔다갔다 횟수
    capacity = M            # 현재 수레의 남은 용량
    while 0 <= i < N + 1:
        # print(cnt)
        if arr[i] >= capacity: # 수레의 용량보다 해당 구역에 당근이 더 많다면
            arr[i] -= capacity # 수레의 용량만큼 해당 구역에서 당근을 지워주고
            cnt += i * 2       # 인덱스의 2배만큼 이동한 것이니 추가
            capacity = M       # 이전에 용량이 채워져서 왔을 수 있으니 초기화
        elif arr[i] <= capacity:    # 수레의 용량이 해당 구역의 당근을 모두 담을 수 있을 만큼 충분하다면
            if i == N:              # 단 마지막 위치라면
                cnt += i * 2        # 그냥 되돌아가도 문제 없으니 해당 거리만큼 추가하고 종료
                break
            capacity -= arr[i]      # 해당 수레의 용량을 채운 만큼 지워줌
            arr[i] = 0              # 다 가져갔으니 해당 구역의 당근 수 0으로
            i += 1                  # 다음 인덱스로 이동
    # print(arr)
    print(f'#{tc} {cnt}')

