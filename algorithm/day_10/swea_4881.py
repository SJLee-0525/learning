def f(idx, N): # 왜 작동하는지 모르겠어요 일단 돼요
    global min_s    # 함수 내부에서 계산해서 내야 시간 초과 안 보는듯
    if idx == N:
        s = 0
        for j in range(N):
            s += arr[j][temp[j]]
        if min_s > s:
            min_s = s
            return
        # r = temp[:] # 그냥 어펜드 하니까 똑같이 나왔는데, 얕은 복사하고 하니까 됨. 왜지> 왜?> 왜ㅙ
        # result.append(r) # 리스트에 다 넣어서 뺸 담에 순회돌리니 런타임 에러 떴음 시간 초과인듯
    else:
        for i in range(idx, N):
            temp[idx], temp[i] = temp[i], temp[idx]  # 순서를 바꾸고
            f(idx + 1, N)   # 바꾼 것을 이용해서 함수 실행
            temp[idx], temp[i] = temp[i], temp[idx]  # 원상 복구해야 예쁘게 나옴. 왜?


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    temp = list(range(N))
    arr = [list(map(int, input().split() )) for _ in range(N)]

    min_s = 101  # 10개에 10보다 작은 수가 나오니
    f(0, N)

    print(f'#{tc} {min_s}')