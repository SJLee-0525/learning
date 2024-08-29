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

def find_code(N, M):
    for j in range(M - 1, -1, -1):
        for i in range(N):
            if code[i][j] == '1':
                end_j = j
                start_i = i
                return (start_i, end_j - 55)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 세로 / 가로
    code = [list(input()) for _ in range(N)]
    start_i, start_j =  find_code(N, M)

    result = []
    for i in range(start_j, start_j + 56, 7):
        result.append(C[''.join(code[start_i][i:i + 7])])

    temp = []
    S = 0
    for r in range(len(result)):
        if r % 2 == 1:
            S += result[r]
        else:
            temp.append(result[r])
    S += sum(temp) * 3

    if S % 10 == 0:
        print(f'#{tc} {sum(result)}')
    else:
        print(f'#{tc} 0')


