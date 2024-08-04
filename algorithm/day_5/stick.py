# 결국 성립되는 괄호 안에 몇 개의 ()가 있는지를 세는 문제
T = int(input())

for test_case in range(1, T + 1):
    space = input()

    # 길이 구하기
    len_space = 0
    for s in space:
        len_space += 1
    
    start, end = 0, 1 # 사용할 인덱스 초기 설정
    cutting = 0 #  총 잘린 개수를 담을 변수 설정

    # for문을 통해 인덱스를 벗어나지 않는 선에서 공간을 탐색
    for start in range(len_space - 1):
        if space[start] == ')': # 만약 시작지점이 ')'라면 볼 것도 없이 다음 반복으로 넘어감
            continue
        else: # 시작지점이 '('인 경우
            judge_count = 1 # 괄호가 끝나는 것을 판단하기 위한 카운트 변수 설정
            laser = 0 # 레이저 수 담을 변수

        for end in range(start + 1, len_space):
            if space[end] == '(': # 만약 '('가 또 나오면 괄호가 끝나지 않으므로 판단 카운트 수를 늘림
                judge_count += 1
            else: # ')'가 나오면 판단 카운트 줄임
                judge_count -= 1
                if judge_count == 0: # 만약 카운트가 0이면 괄호가 끝난 것이므로 마무리 작업 수행
                    if laser != 0: # 레이저가 하나라도 있었다면
                        cutting += laser + 1 # 잘려지는 쇠막대기의 수는 레이저 수 + 1 : 커팅 변수에 추가
                    break
                if space[end - 1:end + 1] == '()': # 만약 end의 바로 앞 문자열과 합쳤을 때 레이저 형식이라면
                    laser += 1 # 레이저 수 추가
                        
    print(f'#{test_case} {cutting}')