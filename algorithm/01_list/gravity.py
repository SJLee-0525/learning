'''
상자들이 쌓여있는 방이 있다. 
방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 떄, 
낙차가 가장 큰 상자를 구하여 낙차를 리턴하는 프로그램을 작성하시오. 
'''
# 9
# 7 4 2 0 0 6 0 7 0

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