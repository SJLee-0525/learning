# LIS 써도 풀 수 있을 것 같은데 구현법을 모르겠음

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pole = [] # 전봇대 넣을 리스트

    cross = 0
    for _ in range(N): 
        left, right = map(int, input().split())
        if pole: # 만약 전봇대 리스트에 전봇대 정보가 있다면
            for vs_left, vs_right in pole: # 뽑아와서 방금 입력한 전봇대랑 비교
                if (left < vs_left and right > vs_right) or (left > vs_left and right < vs_right):
                    cross += 1
        pole.append((left, right))  # 비교 후에는 전봇대 리스트에 추가
    
    print(f'#{tc} {cross}')