T = int(input())
for tc in range(1, T + 1):
    target, pattern = input().split()
 
    cnt = 0 # 타이핑 카운트 변수
    i, j = 0, 0 
    # 각자의 인덱스 범위를 넘어가지 않는 선에서
    while i < len(target) and j < len(pattern): 
        # 만약 둘이 같지 않다면 다음번 순회 때 i는 1 증가하고, j는 0이 되도록 설정
        if target[i] != pattern[j]:
            # 카운트도 늘려줌
            # print('한번', i, j)
            cnt += 1
            i = i - j 
            j = -1
        i += 1 # 만약 값이 같을 경우에 직행할 루트
        j += 1 # 계속 돌면서 길이가 같아질 때 까지 둘이 값이 같다면
        if i == len(target) and j < len(pattern):
            cnt += j
        if j == len(pattern):
            cnt += 1 # 카운트 1회 늘려주고 i값은 그대로 두어 건너뛰게 하고
            j = 0 # j는 0으로 초기화
            if i == len(target) - 1:
                i -= 1  
    
    print(f'#{tc} {cnt}')