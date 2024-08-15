from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 덱의 길이
    deck = list(input().split())

    if N % 2 == 0: # 카드 수가 짝수면
        left = deque(deck[:N // 2])
        right = deque(deck[N // 2:])
    else: # 홀수면
        left = deque(deck[:N // 2 + 1]) # 왼쪽에 하나 더 넣음
        right = deque(deck[N // 2 + 1 :])

    perfect_deck = []
    for count in range(N):
        if count % 2 == 0: 
            perfect_deck.append(left.popleft())
        else:
            perfect_deck.append(right.popleft())
    
    print(f'#{tc}', *perfect_deck)