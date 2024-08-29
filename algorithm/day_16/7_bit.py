T = int(input())
for tc in range(1, T + 1):
    arr = list(input())
    result = []
    for i in range(0, 70, 7):
        temp = ''.join(arr[i:i + 7])
        temp = list(map(int, str(int(temp))))
        temp_v = 0
        op = 1
        for t in range(len(temp) - 1, -1, -1):
            temp_v += int(temp[t]) * op
            op *= 2
        result.append(temp_v)

    print(f'#{tc}', *result)

#
# T = int(input())
# for tc in range(1,T+1):
#     ans_arr = []
#     arr = list(map(int,input()))
#     ans = 0
#     for i in range(70):
#         ans += 2 ** (6 - i%7) * arr[i]
#         if i % 7 == 6:
#             ans_arr.append(ans)
#             ans = 0
#     print(f"#{tc}",*ans_arr)