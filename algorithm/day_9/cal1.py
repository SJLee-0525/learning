cal = {'+': 1, '-': 1, '*': 2, '/': 2}

for tc in range(1, 11):
    N = int(input()) # 문자열 길이
    stack = []
    result = []
    arr = list(input())
    # print(arr)
    for a in arr:
        if a.isdecimal() == True:   # 만약 문자열이 숫자면
            result.append(a)        # result에 삽입
        else:                       # 문자열이 숫자가 아니면: 수식기호면
            if len(stack) == 0:     # 만약 스택이 비어있다면
                stack.append(a)     # 스택에 기호 삽입
            else:                   # 스택에 기호가 있다면
                cal = stack.pop()   # 스택에서 기호 뽑아옴 (원래는 우선순위가 같거나 낮을 떄까지 뽑아야 하지만..)
                stack.append(a)     # 그리고 방금 받은 문자열 기호를 삽입
                if cal == '+':      # 더하기면 덧셈 연산
                    b = int(result.pop())   # 결과 리스트에서 2개 뽑고
                    a = int(result.pop())
                    result.append(a + b)    # 더한 값을 결과 리스트에 반환
    if stack:               # 다 돌고 스택에 기호 남아있으면
        cal = stack.pop()   # 뽑아옴
        if cal == '+':      # 더하기 기호면 마지막으로 연산 한 번 더
            b = int(result.pop())
            a = int(result.pop())
            result.append(a + b)

    print(f'#{tc} {result[0]}')