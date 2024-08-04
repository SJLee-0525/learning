# 이중 루프는 시간 초과 ㅜ

T = int(input())

for test_case in range(1, T + 1):
    space = input()

    # 길이 구하기
    len_space = 0
    for s in space:
        len_space += 1

    stick = 0   # 현재 위치에서의 막대기 수를 담을 변수
    cutting = 0  # 잘린 쇠막대기의 수
    
    for i in range(len_space):
        if space[i] == '(':  # 열린 괄호를 만난 경우
            stick += 1 # 막대기 추가
        else: # 닫힌 괄호를 만난 경우
            if space[i - 1:i + 1] == '()': # 만약 end의 바로 앞 문자열과 합쳤을 때 레이저 형식이라면
                stick -= 1 # 일단 바로 앞에 만들었던 막대기는 줄이고
                cutting += stick  # 현재 막대기 수만큼 잘리니까 그 수 만큼 커팅에 추가

            else:  # 그냥 단일 ')'면
                stick -= 1  # 막대기 하나 줄이고
                cutting += 1  # 잘렸던 안 잘렸던 실제로 하나의 막대기는 추가되니까 넣음
    
    print(f'#{test_case} {cutting}')