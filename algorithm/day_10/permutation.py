def backtrack(a, k, n):  # a 주어진 배열, k 결정할 원소, n 원소 개수
    c = [0] * MAXCANDIDATES

    if k == n:  # 트리의 가장 밑바닥 (위 그림의 경우 k == 3)
        for i in range(0, k):
            print(a[i], end=' ')
        print()
    else:
        # ncandidates (추천된 후보 수)
        ncandidates = construct_candidates(a, k, n, c)  # c: 후보 추천 및 저장
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)

def construct_candidates(a, k, n, c):
    in_perm = [False] * (NMAX + 1)

    for i in range(k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, NMAX + 1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates  # 사용된 적이 없는 원소를 추천해 줘야함


def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end=' ')
    print()


MAXCANDIDATES = 3
NMAX = 3
a = [0] * NMAX
num = [1, 2, 3, 4]
print(backtrack(a, 0, NMAX))