card_list = list(map(int, (input())))  #6676761
card_max = max(card_list)
counts = [0] * (card_max + 1)
print(card_list)

for card_num in card_list:
    counts[card_num] += 1

print(counts) # [0, 0, 0, 0, 0, 0, 4, 2]

for i in range(1, len(counts)):
    counts[i] += counts[i - 1]
print(counts) # [0, 0, 0, 0, 0, 0, 4, 6]

result = [0] * len(card_list)
for re_card_num in card_list[::-1]:
    counts[re_card_num] -= 1
    result[counts[re_card_num]] = re_card_num

print(result)