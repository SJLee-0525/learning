def perm(n, c, arr):
    global result
    if n == c:
        if n == c:
            temp = int(''.join(arr))
            if result < temp:
                result = temp
        return
    else:
        # 순열 조합 계산, j의 범위는 i + 1부터 시작해, i와 j가 중복되는 경우 배제
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]
                perm(n + 1, c, arr)
                arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for tc in range(1, T + 1):
    arr, c = input().split()
    arr = list(arr)

    # 주어진 횟수가 숫자들의 길이보다 클 경우 횟수를 길이로 맞춰줌
    # 굳이 다 바꾸지 않고, 길이만큼만 바꿔도 모든 조합을 생성할 수 있음
    c = int(c)
    if c > len(arr):
        c = len(arr)

    result = 0
    perm(0, c, arr)

    print(f'#{tc} {result}')
