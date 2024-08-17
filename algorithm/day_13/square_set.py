T = int(input())
for tc in range(1, T + 1):
    x1, y1, p1, q1 = map(int, input().split())
    x2, y2, p2, q2 = map(int, input().split())

    if p2 < x1 or q2 < y1 or p1 < x2 or q1 < y2: # 안 겹치는 경우
        rst = 4
    elif (x1 == p2 and y1 == q2) or (x2== p1 and y2 == q1) or (x1 == p2 and y2 == q1) or (x2 == p1 and y1 == q2):
        rst = 3    # 점
    elif x1 == p2 or x2 == p1 or y1 == q2 or y2 == q1: # 선
        rst = 2
    else:           # 면
        rst = 1

    print(f'#{tc} {rst}')