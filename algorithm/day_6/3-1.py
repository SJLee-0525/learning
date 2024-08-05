for tc in range(1, 11):
    find_len = int(input()) # 찾아야 하는 회문 길이
    arr = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(8):  # 인덱스 범위를 넘기지 않기 위해 기준 축 조정
        for j in range(8 - find_len + 1):
            # 가로 검사: 기준 범위에서 M 만큼의 범위를 가진 k를 이용해 회문 검사
            for k in range(find_len // 2):
                if arr[i][j + k] != arr[i][j + find_len - 1 - k]:
                    break
            else: # 잘 풀렸다면 카운트 증가
                cnt += 1

            # 세로 검사: 기준 범위에서 M 만큼의 범위를 가진 k를 이용해 회문 검사
            for k2 in range(find_len // 2):
                if arr[j + k2][i] != arr[j + find_len - 1 - k2][i]:
                    break # 변수 확인 잘 하자 레전드 멍청아
            else: # 잘 풀렸다면 카운트 증가
                cnt += 1

    print(f'#{tc} {cnt}')

