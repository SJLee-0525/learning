T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split()) # N은 부분집합의 개수, K는 목표값

    # 1부터 12까지의 값을 원소로 가진 집합 생성
    arr = list(range(1, 13))
    arr_len = len(arr)
    set_sum_count = 0
    # 2 ** arr_len과 같은 뜻임: 1을 왼쪽으로 2번 밀었다는 뜻 (ex: 0b1 << 2 = 0b100)
    for i in range(1 << arr_len):
        # 요소의 합, 길이 변수 설정
        set_sum = 0
        set_len = 0
        # 일단 더함
        for j in range(arr_len):
            '''
            # i의 j번째 비트가 1이면 True
            j = 0: 1 << j = 1 (0b_001) / 5 & 1 = T (5의 2진수는 101, 첫번째 비트가 1)
            j = 1: 1 << j = 2 (0b_010) / 5 & 2 = F
            j = 2: 1 << j = 4 (0b_100) / 5 & 3 = T
             -> (arr[0]: 3), (arr[2]: 7) 가 출력 
            '''
            if i & (1 << j):
                set_sum += arr[j]
                set_len += 1
        # 부분 집합의 길이가 N과 일치하고 값이 K와 일치하면 카운트 증가
        if set_len == N and set_sum == K:
            set_sum_count += 1

    print(f'#{test_case} {set_sum_count}')
