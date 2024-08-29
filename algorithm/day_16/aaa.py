def move(input_D):
    new_D = {}
    need_check = {}
    for k, v in input_D.items():
        i, j = k
        Q, dir = v
        mi, mj = i + di[dir], j + dj[dir]
        if mi in [0, N - 1] or mj in [0, N - 1]: # 약품 있는 곳에 도달하면
            Q //= 2 # 미생물의 수는 2로 나는 몫으로 줄고
            if Q == 0: # 0이 되면 건너뜀
                continue
            if dir == 1: # 방향이 바뀜
                dir = 2
            elif dir == 2:
                dir = 1
            elif dir == 3:
                dir = 4
            elif dir == 4:
                dir = 3

        if (mi, mj) not in new_D:
            new_D[(mi, mj)] = [Q, dir]
        else:  # 만약 해당 좌표에 미생물이 있다면
            if (mi, mj) not in need_check: # 검사해야 한다고 기록해 둠
                need_check[(mi, mj)] = [new_D[(mi, mj)]]
            need_check[(mi, mj)].append([Q, dir])
            # if new_D[(mi, mj)][0] > Q: # 방향은 양이 많은 쪽의 것을 따르게 되고 (*같은 경우는 주어지지 않음)
            #     dir = new_D[(mi, mj)][1]
            # new_D[(mi, mj)][0] += Q    # 군집 합쳐
            # new_D[(mi, mj)][1] = dir   # 방향 설정

    if need_check:
        for check_key, check_values in need_check.items():
            ci, cj = check_key
            check_values.sort(reverse=True, key=lambda x:x[1])

            M_dir = check_values[0][1]
            Q_sum = 0
            for check_value in check_values:
                Q_sum += check_value[0]
            new_D[(ci, cj)] = [Q_sum, M_dir]

    return new_D

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split()) # N: 한 변 크기, M: 격리 시간, K: 군집 수
    # arr = [[-1] * N] + \
    #       [[-1] + [0] * (N - 2) + [-1] for _ in range(N - 2)] + \
    #       [[-1] * N]

    D = {}

    # 1: 상0, 2: 하1, 3: 좌2, 4: 우3
    di = [0, -1, 1, 0, 0]
    dj = [0, 0, 0, -1, 1]

    for _ in range(K):
        i, j, Q, dir = map(int, input().split())
        D[(i, j)] = [Q, dir] # 최초에 동일한 좌표에 둘 이상의 미생물이 배치되는 경우는 없다함

    for _ in range(M):
        D = move(D)

    result = 0
    print(D)
    for value in D.values():
        result += value[0]

    print(result)

