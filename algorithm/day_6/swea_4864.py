T = int(input())
for tc in range(1, T + 1):
    pattern = input()
    target = input()

    ans = 0
    for i in range(len(target) - len(pattern) + 1):
        cnt = 0
        for j in range(len(pattern)):
            if target[j + i] == pattern[j]:
                cnt += 1
        if cnt == len(pattern):
            ans = 1
    print(f'#{tc} {ans}')
