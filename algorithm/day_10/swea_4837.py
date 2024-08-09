def f(i, V): # V개의 집합에서 i 원소의 포함여부 결정
    if i == V: # 모든 원소에 대해 결정하면
        print(b)
    else:
        b[i] = 1        # a[i] 원소가 부분집합에 포함
        f(i + 1, V)     # 다음 원소를 찾으러 가봐
        b[i] = 0        # a[i] 원소가 부분집합에 포함되지 않음
        f(i + 1, V)

def f2(i, V, K):
    '''부분집합의 합이 K인 경우를 찾아주는 함수'''
    global cnt  # 경우의 수를 셀 용도: 전역설정으로 올리기 위함
    if i == V:
        s = 0   # 합 더하는 변수
        for j in range(V):
            if b[j]: # a[j]가 포함되면
                s += arr[j]
        if s == K:  # 지금까지 모은 부분집합의 합이 K와 같으면
            cnt += 1
        # print(s)
    else:
        b[i] = 1        # a[i] 원소가 부분집합에 포함
        f2(i + 1, V, K)     # 다음 원소를 찾으러 가봐
        b[i] = 0        # a[i] 원소가 부분집합에 포함되지 않음
        f2(i + 1, V, K)

def f3(i, V, N, K): # i 고려할 원소, V 원소 수, N 부분집합 원소 수, K 찾는 힙
    '''부분집합의 요소가 N개이면서 합이 K인 경우를 찾아주는 함수'''
    global cnt  # 경우의 수를 셀 용도: 전역설정으로 올리기 위함
    if i == V:
        s = 0   # 합 더하는 변수
        c = 0   # 개수 더하는 변수
        for j in range(V):
            if b[j]: # a[j]가 포함되면
                s += arr[j]
                c += 1
        if s == K and c == N:  # 지금까지 모은 부분집합의 합이 K와 같고 개수가 N과 같으면
            cnt += 1
        # print(s)
    else:
        b[i] = 1        # a[i] 원소가 부분집합에 포함
        f3(i + 1, V, N, K)     # 다음 원소를 찾으러 가봐
        b[i] = 0        # a[i] 원소가 부분집합에 포함되지 않음
        f3(i + 1, V, N, K)

def f4(i, V, N, K, s): # i 고려할 원소, V 원소 수, N 부분집합 원소 수, K 찾는 힙, s 이전까지 포함된 부분집합 원소 합
    '''가지치기 ver'''
    if i == V:
        global cnt
        if i == V: # 모든 원소 고려
            if s == K: # 부분집합 합이 K인 경우
                cnt += 1
        elif s > K: # 포함된 원소의 합이 이미 목표를 초과한 경우
            return
        else:
            b[i] = 1  # a[i]가 부분집합에 포함되는 경우
            f4(i + 1, V, N, K, s)   # s + a[i]: a[i]를 포함한 경우 원소의 합
            b[i] = 0  # a[i] 원소가 부분집합에 포함되지 않음
            f4(i + 1, V, N, K, s)   # a[i]가 포함되지 않은 경우 원소의 합

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split()) # N 원소의 수 K 집합의 합
    arr = list(range(1, 13))
    b = [0] * 12 # b[i]: a[i] 원소의 포함 여부 표시
    # print(arr)

    # 재ㅔ귀로 모든 부분집합 만들기
    # f(0, 12) # 총 12개의 원소, a[0]부터 포함 여부 결정하기기

    # 부분집합의 합이 K인 경우의 수 찾기
    cnt = 0
    # f2(0, 12, K)
    # print(cnt)
    # f3(0, 12, N, K)

    f4(0, 12, N, K, 0) # 최초에는 원소의 합ㄷ이 0
    print(f'#{tc} {cnt}')
