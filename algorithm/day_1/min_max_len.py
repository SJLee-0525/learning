T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 양수의 개수
    arr = list(map(int, input().split()))

    # 만약 최소값보다 값이 작으면 갱신하고, 인덱스도 갱신
    # 최대값보다 값이 작거나 같으면 갱신하고, 인덱스도 갱신
    min_value = arr[0]
    max_value = arr[0]
    min_index = 0
    max_index = 0
    for index, value in enumerate(arr):
        if min_value > value:
            min_value = value
            min_index = index
        elif max_value <= value:
            max_value = value
            max_index = index

    if max_index - min_index < 0:
        print(f'#{test_case} {-(max_index - min_index)}')
    else:
        print(f'#{test_case} {(max_index - min_index)}')