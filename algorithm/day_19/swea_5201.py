T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 컨테이너 N, 트럭 수 M
    w_list = list(map(int, input().split())) # 컨테이너 무게
    t_list = list(map(int, input().split())) # 트럭 적재 용량

    # 컨테이너 무게, 트럭 적재 용량 내림차순 정렬
    w_list.sort(reverse=True)
    t_list.sort(reverse=True)

    weight = 0      # 결과 변수
    temp_n = 0      # 인덱스 조정 할 때 쓸 변수
    for t in range(M):  # 트럭 리스트 순회
        for w in range(temp_n, N):  # temp_n부터 컨테이너 무게 순회
            if t_list[t] >= w_list[w]:  # 만약 트럭 적재 용량이 컨테이너 수용 가능하다면
                weight += w_list[w]     # 결과 변수에 무게 추가해 주고
                temp_n = w + 1          # 방금 탐색한 w까지는 더 이상 탐색할 이유 없으니 temp_n 재할당
                break                   # 다음 트럭으로

    print(f'#{tc} {weight}')
