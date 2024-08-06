def my_push(gh, size): # push 함수 만들기
    global top
    top += 1
    if top == size: # 스택이 꽉 차서 못 들어가면 False 반환
        return False
    else: # 아니라면 작업 수행
        stack[top] = gh
        return 0

def my_pop(): # pop 함수 만들기
    global top
    if top == -1: # 만약 스택이 비었으면 False 반환
        return False
    else: # 아니라면 작업 수행
        top -= 1
        return stack[top + 1]

T = int(input())

for tc in range(1, T + 1):

    size = 50 # 최대 문자열의 길이가 50이랬으니까
    stack = [0] * size
    top = -1

    S = input()
    for word in S: # 좌측 괄호가 있으면 스택에 push
        if word in ['(', '{', '[']:
            my_push(word, size)
        elif word in [')', '}', ']']: # 우측 괄호가 있으면 pop
            temp = my_pop()
            if temp == 0: # 만약 pop 반환 값이 0이면 (스택이 빈 공간이라면)
                print(f'#{tc} 0') # 출력 후 정지
                break
            else: # 만약 스택에 자료가 있었다면
                if word == ')': # 우괄호가 소괄호인데
                    if '(' != temp: # pop한 괄호가 소괄호가 아니면
                        print(f'#{tc} 0') # 종료
                        break
                elif word == '}': # 우측 괄호가 중괄호인데
                    if '{' != temp: # pop한 자료가 중괄호가 아니면
                        print(f'#{tc} 0') # 종료
                        break
                elif word == ']': # 그만쓰자 힘들다
                    if '[' != temp:
                        print(f'#{tc} 0')
                        break

    else: # 만약 어찌저찌 문제없이 잘 통과했는데
        if top == -1: # 스택까지 잘 비어있으면
            print(f'#{tc} 1') # 너는 완벽한 괄호야
        else: # 만약 스택에 괄호가 남아있으면
            print(f'#{tc} 0') # 빠이