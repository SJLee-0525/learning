def perm(i, K):
    global max_r, min_r
    if i == K:
        result = cal_perm(op_list, K)
        if max_r < result:
            max_r = result
        if min_r > result:
            min_r = result
    else:
        used = set() # 현재 재귀 단계에서 중복되는 연산자를 방지하기 위한 set집합 생성
        for j in range(i, K):
            if op_list[j] not in used:  # 현재 j위치의 연산자가 used에 포함돼 있는지 확인. 포함돼 있다면 이 연산자로 시작하는 순열을 생성한 것이므로 건너뜀
                used.add(op_list[j])    # 없다면 used에 추가하고 재귀 호출, 이러면 다음 재귀 호출에서는 이 연산자로 시작하는 다른 순열이 생기지 않음
                op_list[i], op_list[j] = op_list[j], op_list[i]     # i와 j위치의 연산자를 교환해 새 순열 생성
                perm(i + 1, K)                                      # 완성되지 않았다면 재귀를 통해 다음 위치에서의 순열 생성 지속
                op_list[i], op_list[j] = op_list[j], op_list[i]     # 재귀 호출 후 원상태로 되돌려 다음 순열 생성을 준비

def cal_perm(input_op, K):
    global arr
    r = arr[0]
    for i in range(K):
        if input_op[i] == 0:
            r += arr[i + 1]
        elif input_op[i] == 1:
            r -= arr[i + 1]
        elif input_op[i] == 2:
            r *= arr[i + 1]
        elif input_op[i] == 3:
            if r < 0:
                r = -(abs(r) // arr[i + 1])
            else:
                r //= arr[i + 1]
    return r

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    operators = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    op_list = [i for i, j in enumerate(operators) if j for _ in range(j)]
    # 연산자 수에 맞춰서 연산자 나열하기
    # 0 : +, 1 : -, 2 : *, 3 : /

    max_r = -100000000
    min_r = 100000000
    perm(0, N - 1)

    print(f'#{tc} {max_r - min_r}')