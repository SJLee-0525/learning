T = int(input())
for tc in range(1, T + 1):
    time_table = []
    N = int(input())
    for _ in range(N): # 각 화물차들의 시작, 완료시간을 타임테이블에 담아줌
        time_table.append(tuple(map(int, input().split())))

    time_table.sort(key=lambda x:x[1])  # 종료 시간을 기준으로 오름차순 정렬

    end = time_table[0][1]  # 초기 end 값은 첫차의 완료 시간으로 지정
    cnt = 1                 # 첫 차는 이미 카운트 됐으니 1 할당하고 시작
    for i in range(1, N):   # 0을 제외한 타임테이블 인덱스 순회
        if time_table[i][0] >= end: # 만약 end값보다 time_table[i]의 시작지점이 크다면
            cnt += 1                # 카운트 증가
            end = time_table[i][1]  # end 값은 해당 화물차의 완료 시점으로 재할당

    print(f'#{tc} {cnt}')
