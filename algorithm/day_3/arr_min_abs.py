'''
N*N 배열의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하고,
각 요소의 절대값의 합을 모두 조사한 총합을 구하시오
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
abs_min_total = 0

# N * N 배열의 모든 원소에 대해
for i in range(N):
    for j in range(N):
        # i, j의 4방향 원소에 대해
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # ni, nj의 값이 인덱스 범위를 넘어가지 않게끔
            if 0 <= ni < N and 0 <= nj < N:
			          # 해당 원소와 인접한 원소의 차의 절대값 구하기
                temp = arr[i][j] - arr[ni][nj]
                if temp < 0:
                    temp *= -1
                abs_min_total += temp

print(abs_min_total)