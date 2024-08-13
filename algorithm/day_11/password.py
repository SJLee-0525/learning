from collections import deque
for _ in range(10):
    tc = int(input())
    pw = deque(map(int, input().split()))

    while pw[-1] != 0:
        for i in range(1, 6):
            temp = pw.popleft() - i
            if temp > 0:
                pw.append(temp)
            else:
                pw.append(0)
                break

    print(f'#{tc}', end=' ')
    for i in range(8):
        print(pw[i], end =' ')
    print()