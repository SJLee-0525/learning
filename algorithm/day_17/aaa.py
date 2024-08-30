import sys
sys.stdin = open("./sample_input.txt", "r")

C = {'0001101': 0,
     '0011001': 1,
     '0010011': 2,
     '0111101': 3,
     '0100011': 4,
     '0110001': 5,
     '0101111': 6,
     '0111011': 7,
     '0110111': 8,
     '0001011': 9}

def find_start(N, MR):
    i, j = 0, MR - 1
    while i < N:
        if CODE[i][j] == '1':
            end = j
            while 0 <= j:
                j -= 56
                if CODE[i][j - 1] == '0':
                    break
            # print(j, end)
            pw = ''.join(CODE[i][j + 1:end + 1])
            CODE_set.add(pw)
        j -= 1
        if j < 0:
            i += 1
            j = MR - 1

#####################################################################

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N개의 줄
    CODE = []
    for _ in range(N):
        init_input = list(input())
        R_list = []
        for c in range(M):
            b_c = bin(int(init_input[c], 16))[2:]
            temp = ['0', '0', '0', '0']
            for i in range(len(b_c)):
                temp[4 - len(b_c) + i] = b_c[i]
            R_list.extend(temp)
        CODE.append(R_list)

    CODE_set = set()
    MR = len(R_list)

    find_start(N, MR)

    # print(CODE_set)

    pure_pw = []
    for pw in CODE_set:
        temp = []
        # print(pw)
        # print('aaa', len(pw))
        c_score = len(pw) // 56
        for i in range(0, len(pw), c_score):
            temp.append(pw[i])
        pure_pw.append(''.join(temp))

    print('pure', pure_pw)
    result = 0
    for p_pw in pure_pw:
        r = []
        for i in range(0, 56, 7):
            key = ''.join(p_pw[i:i + 7])
            if key in C:
                r.append(C[''.join(p_pw[i:i + 7])])
        # print(r)
        holsu = 0
        jjaksu = 0

        print(r)
        for rr in range(7):
            if rr % 2 == 0: ## 홀수
                holsu += r[rr]
            else:
                jjaksu += r[rr]
        temp_result = holsu * 3 + jjaksu + r[7]
        if temp_result % 10 == 0:
            result += sum(r)

    else:
        print(f'#{tc} {result}')




