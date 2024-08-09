def backtrack(a, k, n):  # a 주어진 배열, k 결정할 원소, n 원소 개수
    c = [0] * MAXCANDIDATES

    if k == n:  # 트리의 가장 밑바닥 (위 그림의 경우 k == 3)
        process_solution(a, k)  # 답이면 원하는 작업을 한다
    else:
        # ncandidates (추천된 후보 수)
        ncandidates = construct_candidates(a, k, n, c)  # c: 후보 추천 및 저장
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)


def construct_candidates(a, k, n, c):
    c[0] = True
    c[1] = False
    return 2


def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end=' ')
    print()


MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
num = [1, 2, 3, 4]
print(backtrack(a, 0, NMAX))