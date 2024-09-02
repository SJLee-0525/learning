def combi(n, N):
    '''바꿀 조합 생성'''
    if n == N:
        if sum(b) == 2:
            temp = []
            for j in range(N):
                if b[j]:
                    temp.append(j)
            combi_list.append(temp)
        return
    b[n] = 0
    combi(n + 1, N)
    b[n] = 1
    combi(n + 1, N)

def perm(n, N, c):
    if n == c:
        # print(perm_list)
        make_num(perm_list, c)
        return
    for i in range(N):
        perm_list.append(combi_list[i])
        perm(n + 1, N, c)
        perm_list.pop()

def make_num(i_perm, c):
    global result
    i_arr = arr
    for x, y in i_perm:
        i_arr[x], i_arr[y] = i_arr[y], i_arr[x]
    temp = int(''.join(i_arr))
    if result < temp:
        result = temp

T = int(input())
for tc in range(1, T + 1):
    arr, c = input().split()
    arr, c = list(arr), int(c)
    # print(c, arr)
    result = 0

    combi_list = []
    b = [0] * len(arr)
    combi(0, len(arr))

    # print('combi', combi_list)

    perm_list = []
    perm(0, len(combi_list), c)
    # print('perm', perm_list)

    print(f'#{tc} {result}')