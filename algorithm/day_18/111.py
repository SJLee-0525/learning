
def perm(n, N, c):
    if n == c + 1:
        print(perm_list)
        make_num(perm_list, c)
        return
    for i in range(N):
        perm_list.append(arr_list[i])
        perm(n + 1, N, c)
        perm_list.pop()

def make_num(i_perm, c):
    global result
    i_arr = arr[:]
    for i in range(c):
        i_arr[i_perm[i]], i_arr[i_perm[i + 1]] = i_arr[i_perm[i + 1]], i_arr[i_perm[i]]
    temp = int(''.join(i_arr))
    if result < temp:
        result = temp

T = int(input())
for tc in range(1, T + 1):
    arr, c = input().split()
    arr, c = list(arr), int(c)
    arr_list = list(range(len(arr)))

    L = len(arr)
    # print(c, arr)
    result = 0
    #
    # combi_list = []
    # b = [0] * len(arr)
    # combi(0, len(arr))

    # print('combi', combi_list)

    perm_list = []
    perm(0, L, c)
    # print('perm', perm_list)

    print(f'#{tc} {result}')