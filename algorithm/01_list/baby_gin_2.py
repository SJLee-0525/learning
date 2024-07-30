T = int(input())

for test_case in range(1, T + 1):
    card_arr = list(map(int, input()))

    # 카드 배열에서 가장 큰 값 찾기
    card_max = card_arr[0]
    for card_num in card_arr:
        if card_max < card_num:
            card_max = card_num

    # 카드 번호를 인덱스로, 개수를 값으로 하는 리스트 생성
    counts = [0] * (card_max + 1)
    for card_num in card_arr:
        counts[card_num] += 1

    # 3이상인 값이 있으면 triplet
    for index in range(card_max + 1):
        while counts[index] >= 3:
            counts[index] -= 3

    # 연속으로 3개가 1 이상이면 run!
    for index_2 in range(card_max - 1):
        while counts[index_2] > 0:
            if counts[index_2] >= 1 and counts[index_2 + 1] >= 1 and counts[index_2 + 2] >= 1:
                counts[index_2] -= 1
                counts[index_2 + 1] -= 1
                counts[index_2 + 2] -= 1
            else:
                break

    # 마지막으로 남은 counts의 합계 구하기
    test_sum = 0
    for fin_count in counts:
        test_sum += fin_count

    # 합계가 0이면 Baby-Gin, 아니면 패배
    if test_sum == 0:
        print(f'#{test_case} Baby Gin')
    else:
        print(f'#{test_case} Lose')
