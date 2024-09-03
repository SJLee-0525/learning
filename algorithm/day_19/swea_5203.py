def check(p, n):
    '''babygin, triplet 체크'''
    for i in range(10):
        # 같은 카드가 3장 이상 있으면
        if p[i] >= 3:
            return n
        # 연속된 세 카드가 있으면
        if i <= 7 and (p[i] >= 1 and p[i + 1] >= 1 and p[i + 2] >= 1):
            return n
    else:
        return 0

####################################################################

T = int(input())
for tc in range(1, T + 1):
    card_seq = list(map(int, input().split()))
    player_1 = [0] * 10
    player_2 = [0] * 10

    for i in range(6): # 각 입력마다 함수 돌려야 에러 안 남. 이유는 모르겠음
        player_1[card_seq[i * 2]] += 1
        rst = check(player_1, 1)
        if rst:     # 만약 리턴 값이 있으면 중단
            break
        player_2[card_seq[i * 2 + 1]] += 1
        rst = check(player_2, 2)
        if rst:
            break

    print(f'#{tc} {rst}')