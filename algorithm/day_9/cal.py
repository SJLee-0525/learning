# cal = {'+': 1, '-': 1, '*': 2, '/': 2}

T = int(input())
for tc in range(1, T + 1):
    c_arr = list(input().split())
    c_stack = []

    for c in c_arr:
        if c == '.':
            if len(c_stack) == 1:
                # 1 이상인 경우로 하면 테케 오류남. 만약 마지막에 .이 왔는데 스택에 자료가 남아있으면 그 연산은 잘못된 것임.
                # 진짜 치사하네 증말
                result = int(c_stack.pop())
                break
            else:
                result = 'error'
                break
        elif c == '+':
            if len(c_stack) >= 2: # 뽑을 자료가 2개 이상인 경우에만
                b = int(c_stack.pop())
                a = int(c_stack.pop())
                c_stack.append(a + b)
            else: # 만약 부족하면 에러
                result = 'error'
                break
        elif c == '-':
            if len(c_stack) >= 2:
                b = int(c_stack.pop())
                a = int(c_stack.pop())
                c_stack.append(a - b)
            else:
                result = 'error'
                break
        elif c == '*':
            if len(c_stack) >= 2:
                b = int(c_stack.pop())
                a = int(c_stack.pop())
                c_stack.append(a * b)
            else:
                result = 'error'
                break
        elif c == '/':
            if len(c_stack) >= 2:
                b = int(c_stack.pop())
                a = int(c_stack.pop())
                c_stack.append(a // b)
            else:
                result = 'error'
                break
        else:
            c_stack.append(c)

    if not result == 'error':
        result = int(result) # 정수형 변환

    print(f'#{tc} {result}')
