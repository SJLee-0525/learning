T = int(input())

for test in range(1, T + 1):
    K, N, M = map(int, input().split())
    gas_stations = list(map(int, input().split()))
    station_map = [0] * (N + 1)

    for gas_station in gas_stations:
        station_map[gas_station] = gas_station
    print(station_map)

    judge = True
    start, end = 0, K + 1
    charge_count = 0
    while end <= N:
        if max(station_map[start + 1:end]) == 0:
            judge = False
            break
        elif max(station_map[start + 1:end]) != 0:
            start = max(station_map[start:end])
            end = start + K + 1
            charge_count += 1
    
    if judge == False:
        print(f'#{test} 0')
    else:
        print(f'#{test} {charge_count}')

