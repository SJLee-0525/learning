T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_carrot = 0
    for i in range(N):
        if max_carrot < arr[i]:
            max_carrot = arr[i]
            max_district = i + 1
    
    print(f'#{tc} {max_district} {max_carrot}')