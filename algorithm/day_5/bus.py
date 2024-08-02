T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 버스 노선의 개수

    # 버스 범위에 맞춰서 정류장 Range 설정 후 dict에 등장한 수만큼 삽입
    station_dict = {}
    for i in range(1, N + 1):
        start, end = map(int, input().split())
        for station in range(start, end + 1):
            if station not in station_dict:
                station_dict[station] = 1
            else:
                station_dict[station] += 1

    P = int(input())
    # 테스트 케이스 출력 후, 입력되는 값에 따라 딕셔너리 값 출력
    print(f'#{test_case} ', end ='')
    for _ in range(P):
        target = int(input())
        print(station_dict.get(target, 0), end=' ')
    print()
