T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 입력되는 길이
    num = input()
    max_count = 0

    max_count = 0
    count = 0
    for n in num:
        if n == '1':
            count += 1
        else:
            count = 0
            continue
        if max_count <= count:
            max_count = count

    print(f'#{test_case} {max_count}')
