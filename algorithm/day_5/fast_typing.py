T = int(input())

for test_case in range(1, T + 1):
    A, B = input().split()

    # 탐색을 위해 각각의 길이 구하기
    A_len = 0
    for _ in A:
        A_len += 1

    B_len = 0
    for _ in B:
        B_len += 1

    # 인덱스 값 설정
    i = 0
    count = 0
    # 인덱스가 초과하지 않는 선에서
    # B와 일치하는 부분이 있으면 1개만 늘리고 건너뜀
    # 없으면 한개씩 늘리면서 증가
    while i < A_len:
        if 0 <= i < A_len - B_len + 1 and A[i:i + B_len] == B:
            count += 1
            i += B_len
        else:
            count += 1
            i += 1

    print(f'#{test_case} {count}')
