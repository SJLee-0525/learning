T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 당근의 개수
    capacity = N // 2
    arr = list(map(int, input().split()))

    max_carrot = 0      # 카운트 하기 위해서 max값을 찾아봄
    for a in arr:
        if max_carrot < a:
            max_carrot = a

    count = [0] * (max_carrot + 1) # [0, 1, 1, 1, 1, 1, 1, 1, 1]

    for a2 in arr:      # 당근의 크기를 인덱스, 당근 수를 값으로 
        count[a2] += 1

    judge = False        # 마지막 출력 떄 사용할 것
    # print(capacity, count)

    for c in count:     # 같은 값을 가지는 당근이 용량보다 많으면 false
        if c > capacity:
            break
    
    ans = 1001            # 정답 변수: 당근 하나의 최대 수량이 1000이니까 
    for i in range(max_carrot):              # 3분할 하기 위해서 2중 for문 사용
        for j in range(i + 1, max_carrot + 1):
            # print(i, j)
            small_box = 0                           # i를 기준으로 앞 부분은 작은 박스
            for small in range(i):
                small_box += count[small]
            if small_box == 0 or small_box > capacity:  # 만약 용량보다 많거나, 1개도 들지 않았다면 다음 루프로
                continue
            
            mid_box = 0
            for mid in range(i, j):                 # i와 j 사이의 부분은 중간 박스
                mid_box += count[mid]
            if mid_box == 0 or mid_box > capacity:
                continue

            big_box = 0
            for big in range(j, max_carrot + 1):    # j를 기준으로 이후는 큰 박스
                big_box += count[big]
            if big_box == 0 or big_box > capacity:
                continue
            
            # print('@@@', [small_box, mid_box, big_box])

            min_d, max_d = 1001, -1                  # 최소값, 최대값 측정
            for box in [small_box, mid_box, big_box]:
                if min_d > box:
                    min_d = box
                if max_d < box:
                    max_d = box
            temp_d = max_d - min_d                  # 둘의 차이의 최소값을 확인 후 할당
            if ans >= temp_d:
                ans = temp_d
                judge = True                        # 여기 까지 왔다면 적어도 담을 수 있는 경우가 하나라도 있는 것이므로 True로 전환
           
    if judge == True:                               # 만약 개수 초과가 없었다면 차이를 출력
        print(f'#{tc} {ans}')
    else:                                           # 초과가 한 번이라도 있었다면(judge == False)
        print(f'#{tc} -1')

