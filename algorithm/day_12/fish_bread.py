T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    # N 사람수, M 초, K 개수
    customer = list(map(int, input().split()))

    latest_time = 0
    for c in customer:
        if latest_time < c:
            latest_time = c

    # 해당 시간에 만들 수 있는 붕어빵 타임라인 만들기
    bread_timeline = [0] * (latest_time + 1)
    for i in range(1, latest_time + 1):
        if i % M == 0:
            bread_timeline[i] += K

    # 누적합 만들기
    for i2 in range(1, latest_time + 1):
        bread_timeline[i2] += bread_timeline[i2 - 1]
    # print(bread_timeline) # [0, 0, 2, 2, 4]

    # 해당 시간에 필요한 붕어빵 개수와 관련된 타임라인
    visit_timeline = [0] * (latest_time + 1)
    for visit_time in customer:
        visit_timeline[visit_time] = 1

    # 누적합 만들기
    for i3 in range(1, latest_time + 1):
        visit_timeline[i3] += visit_timeline[i3 - 1]
    # print(visit_timeline) # [0, 0, 0, 1, 2]

    # 시간대별로 돌면서 비교: 만약 해당 시간대에 빵 타임라인 - 방문 타임라인이 음수면 손님은 기다려야 함
    for j in range(latest_time + 1):
        if bread_timeline[j] - visit_timeline[j] < 0:
            print(f'#{tc} Impossible')
            break
    else:
        print(f'#{tc} Possible')