T = int(input())
for tc in range(1, T + 1):
    target, pattern = input().split()

    cnt = 0
    i = 0
    while i < len(target):
        if i + len(pattern) <= len(target) and target[i:i + len(pattern)] == pattern:
            i += len(pattern)
            cnt += 1
        else:
            i += 1
            cnt += 1

    print(f'#{tc} {cnt}')