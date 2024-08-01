# T = int(input())

# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))

# 버블
#     for i in range(N - 1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             print(arr)

# 카운팅
    # max_value = arr[0]
    # for value in arr:
    #     if max_value < value:
    #         max_value = value
        
    # counting_list = [0] * (max_value + 1)

    # for value in arr:
    #     counting_list[value] += 1
    
    # for i in range(1, max_value + 1):
    #     counting_list[i] += counting_list[i - 1]
    
    # result_list = [0] * N
    # for rev_value in arr[::-1]:
    #     counting_list[rev_value] -= 1
    #     result_list[counting_list[rev_value]] = rev_value
    
    # print(result_list)

    # 선택 정렬
    # for i in range(N - 1):
    #     min_index = i
    #     for j in range(i + 1, N):
    #         if arr[min_index] > arr[j]:
    #             min_index = j
    #     arr[i], arr[min_index] = arr[min_index], arr[i]
    # print(arr)

# 순열
# arr = [1, 2, 3, 4, 5]
# N = 5

# for i in range(1<<N):
#     mini_set = []
#     for j in range(N):
#         if i & (1<<j):
#             mini_set.append(arr[j])
#     print(mini_set)

# 순차 검색
arr = [4, 9, 11, 23, 2, 19, 7]
target = 4

i = 0
while i < len(arr) and arr[i] != target:
    i += 1
if i < len(arr):
    print(i)
else:
    print(-1)

# 정렬된 경우
arr2 = [2, 4, 7, 9, 11, 19, 23]
target2 = 1
i2 = 0

while i2 < len(arr2) and arr2[i2] < target2:
    i2 += 1
if i2 < len(arr2) and arr2[i2] == target2:
    print(i2)
else:
    print(-1)

# 이진 검색
arr3 = [2, 4, 7, 9, 11, 19, 23]
target3 = 11

start, end = 0, len(arr3) - 1
while start <= end:
    mid = (start + end) // 2
    if target3 == arr3[mid]:
        print(mid)
        break
    elif target3 > arr3[mid]:
        start = mid + 1
    elif target3 < arr3[mid]:
        end = mid - 1

if target3 != arr3[mid]:
    print(-1)
