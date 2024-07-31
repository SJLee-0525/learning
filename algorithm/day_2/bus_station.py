T = int(input())

for test in range(1, T + 1):
    K, N, M = map(int, input().split())
    # N = 종점, K = 충전 이동 거리, M = 충전기 수
    gas_stations = list(map(int, input().split()))
    station_map = [0] * (N + 1)

    # 정류장의 수만큼 배열을 생성하고 충전기가 설치된 정류장에 값을 입력
    for gas_station in gas_stations:
        station_map[gas_station] = gas_station
    # print(station_map)

    # 포인터 설정
    judge = True
    start, end = 0, K + 1
    charge_count = 0
    while end <= N:
        count = 0
        # 현재 위치에서 갈 수 있는 범위 내의 값을 더함
        for station in station_map[start + 1:end]:
            count += station
        # 합이 0이면 충전기가 없다는 뜻이니 FAIL
        if count == 0:
            judge = False
            break
        # 0이 아니라면 충전기가 있다는 뜻이니 start를 충전기 위치로 변경, 충전 횟수 증가
        elif count != 0:
            max_station = station_map[start]
            for station_2 in station_map[start:end]:
                if max_station < station_2:
                    max_station = station_2
            start = max_station
            end = start + K + 1
            charge_count += 1

    if judge == False:
        print(f'#{test} 0')
    else:
        print(f'#{test} {charge_count}')