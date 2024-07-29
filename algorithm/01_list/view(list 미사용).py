# 최대값 구할 때 리스트 쓰지 말아보기
for test in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    great_view = 0
    for target_index in range(2, N - 2):
        nearby_tall = arr[target_index - 2]
        for nearby_index in range(target_index - 2, target_index + 3):
            if nearby_index == target_index:
                continue
            if nearby_tall < arr[nearby_index]:
                nearby_tall = arr[nearby_index]
        
        if arr[target_index] - nearby_tall > 0:
            great_view += arr[target_index] - nearby_tall
    
    print(f'#{test} {great_view}')