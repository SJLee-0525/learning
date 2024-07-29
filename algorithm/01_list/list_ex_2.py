n = int(input())
arr = list(map(int, input().split()))

fall_list = []
for index, num in enumerate(arr):
    count = 0
    for i in range(index + 1, len(arr) - 1):
        count += 1
        if arr[i] >= num:
            fall_list.append(count)
            break

print(fall_list)
max_value = fall_list[0]
for fall in fall_list:
    if max_value < fall:
        max_value = fall

print(max_value)