T = int(input())

score_count = {}

for _ in range(T):
    test_case = int(input())
    score_arr = list(map(int, input().split()))

    # 카운트 정렬
    count = [0] * 101
    for score in score_arr:
        count[score] += 1

    for i in range(1, 101):
        count[i] += count[i - 1]

    sorted_score_arr = [0] * 1000
    for rev_score in score_arr[::-1]:
        count[rev_score] -= 1
        sorted_score_arr[count[rev_score]] = rev_score

    # 최빈값 구하기
    max_count = 0
    for i in range(999):
        j = i + 1
        if sorted_score_arr[i] == sorted_score_arr[j]:
            count = 1
            while j < 1000 and sorted_score_arr[i] == sorted_score_arr[j]:
                j += 1
                count += 1
            if max_count <= count:
                max_count = count
                max_value = sorted_score_arr[i]

    print(f'#{test_case} {max_value}')