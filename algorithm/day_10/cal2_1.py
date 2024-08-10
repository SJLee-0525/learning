d = {'+': 1, '-': 1, '*': 2, '/': 2}
 
for tc in range(1, 11):
    N = int(input()) # 식 길이
    infix_notation = list(input())
    stack = []
    postfix_notation = []
    for a in infix_notation:
        if a in d: # a가 기호라면
            if stack: # 스택에 기호가 하나라도 있다면
                if d[a] > d[stack[-1]]:    # 만약 스택의 마지막에 있는 기호보다 우선 순위가 높다면
                    stack.append(a)         # 스택에 넣음
                else:                       # 스택의 마지막에 있는 기호보다 우선 순위가 낮거나 같다면
                    while len(stack) >= 1 and d[a] <= d[stack[-1]]: # 스택의 마지막에 있는 기호보다 작은 동안
                        postfix_notation.append(stack.pop())        # 스택 자료를 뽑아서 후위 표기식에 넣음
                    stack.append(a)                                 # 위 조건을 탈출하면 해당 연산자를 스택에 삽입
            else:   # 스택에 기호가 없다면 (우선순위 따질 것이 없음) 스택에 기호 ㄴ넣음
                stack.append(a)
        else: # 기호가 아니라면 (== 숫자라면)
            postfix_notation.append(int(a)) # 나중에 편하게 정수로 바꿔서 후위 표기식에 넣음
 
    while len(stack) >= 1: # 다 돌고 나서 스택에 남아있는 자료가 있다면
        postfix_notation.append(stack.pop()) # 비워질 때까지 뽑음
 
    # print(stack)
    # print(postfix_notation)
    # print(len(postfix_notation))
 
    # 후위표기식을 계산하기
    result = []
    b = True
    for a2 in postfix_notation:
        if a2 in d: # 기호면
            # print(result, a2)
            if len(result) >= 2:    # result에서 두개 뽑아서 기호에 맞춰 연산
                y = result.pop()    # 순서 확인 잘 하기
                x = result.pop()
                if a2 == '+':
                    result.append(x + y)
                elif a2 == '-':
                    result.append(x - y)
                elif a2 == '*':
                    result.append(x * y)
                elif a2 == '/':
                    result.append(x // y)
            else: # 만약 result 리스트에 요소가 2개가 밑이라면 잘못된 식이므로 중단
                b = False
                break
        else: # 기호가 아니면 == 숫자면
            result.append(a2)
 
    if b == True:
        if len(result) == 1: # 알맞게 계산이 돼 result 리스트에 자료가 하나만 남아있다면
            print(f'#{tc} {result[0]}')
        else:
            print(f'#{tc} -1')