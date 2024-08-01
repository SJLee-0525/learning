T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 주어지는 배열의 길이
    arr = list(map(int, input().split()))

    # 선택 정렬
    for i in range(N - 1):
        # 반복마다 최소 인덱스값을 시작값으로 할당
        min_index = i
        for j in range(i + 1, N):
            # 만약 현재 j가 가리키는 값이 기존 최소값보다 작으면 j를 min_index에 할당
            if arr[min_index] > arr[j]:
                min_index = j
        # 다 돌면 교환
        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(f'#{test_case} ', end='')
    for elem in arr:
        print(elem, end=' ')
    print()