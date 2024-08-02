code_d = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
code_d_reverse = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}

T = int(input())
for _ in range(T):
    test_case, arr_len = input().split()
    # 길이가 문자열이니 int로 형변환
    arr_len = int(arr_len)

    arr = list(input().split())

    # arr를 순회하며 code_d 딕셔너리를 이용해서 해당 키에 해당하는 값으로 바꿈
    for index in range(arr_len):
        arr[index] = code_d[arr[index]]

    # # 선택정렬
    # for i in range(arr_len - 1):
    #     min_index = i
    #     for j in range(i, arr_len):
    #         if arr[min_index] > arr[j]:
    #             min_index = j
    #     arr[i], arr[min_index] = arr[min_index], arr[i]

    # 카운팅 정렬로도 해보기
    count = [0] * 10
    for elem in arr:
        count[elem] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    new_arr = [0] * arr_len
    for rev_elem in arr[::-1]:
        count[rev_elem] -= 1
        new_arr[count[rev_elem]] = rev_elem

    # 정렬 arr를 code_d_reverse 딕셔너리를 이용해 해당 키에 해당하는 값으로 바꿈
    for index2 in range(arr_len):
        new_arr[index2] = code_d_reverse[new_arr[index2]]

    print(test_case)
    print(*new_arr)