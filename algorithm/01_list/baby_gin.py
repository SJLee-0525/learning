card_list = list(map(int, (input()))) #6676761
card_max = max(card_list)
counts = [0] * (card_max + 1)
print(card_list)

for card_num in card_list:
    counts[card_num] += 1

print(counts) # [0, 0, 0, 0, 0, 0, 4, 2]
# 3이상인 값이 있으면 triplet
for i in range(len(counts)):
    while counts[i] >= 3:
        counts[i] -= 3
        print('tryplet')

# 연속으로 3개가 1 이상이면 run!
for i in range(len(counts) - 2):
    if counts[i] > 0 and counts[i + 1] > 0 and counts[i + 2] > 0:
        counts[i] -= 1
        counts[i + 1] -= 1
        counts[i + 2] -= 1
        print('run')

if sum(counts) == 0:
    print('win')
else:
    print('lose')