def perm(i, N, temp):
    '''모든 외계인들이 줄을 서는 경우를 만드는 순열 함수'''
    global result
    if i >= 2: # 만약 점수를 계산할 수 있는 시점이 오면
        temp += arr[EL[i - 2]][EL[i - 1]] # 일단 계산하고
        if result < temp: # 만약 현재 최소 값보다 방금 계산한 점수가 높으면
            return  # 더 이상 순열을 생성하지 않고 돌아감
    if i == N: # 끝까지 와서 더 이상 바꿀 공간이 없으면
        if result > temp: # 현재 최소 값과 비교
            result = temp # 더 낮으면 값 변환
    else:
        for j in range(i, N):
            EL[i], EL[j] = EL[j], EL[i]
            perm(i + 1, N, temp) # 재귀
            EL[i], EL[j] = EL[j], EL[i]

################################################################

T = int(input()) # 테스트 케이스 개수

for tc in range(1, T + 1):
    N = int(input())  # 외계인의 수
    arr = [list(map(int, input().split())) for _ in range(N)] # 위험도 배열

    EL = list(range(N)) # 외계인 번호를 담은 리스트 생성 [0, 1, 2]

    result = 100001 # 결과값 할당
    perm(0, N, 0) # 순열 함수 호출

    print(f'#{tc} {result}')