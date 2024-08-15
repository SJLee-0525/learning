T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 버스 노선 수
    bus_route = [tuple(map(int, input().split())) for _ in range(N)]
    # 노선의 시작점과 종점을 튜플로 구분해 리스트에 담음

    farthest_station = max(bus_route, key=lambda x:x[1])[1]
    # 버스가 다니는 정류장 중에서 가장 먼 정류장을 가져옴

    station_map = [0] * (farthest_station + 1)
    # 지도 생성 후 순회하면서 정류장마다 다니는 버스 노선 수를 추가
    for start, end in bus_route:
        for stop in range(start, end + 1):
            station_map[stop] += 1
            
    print(station_map)
    print(f'#{tc}', end=' ')
    P = int(input())
    for _ in range(P):
        ii = int(input())
        print(station_map[ii], end=' ')
    print()