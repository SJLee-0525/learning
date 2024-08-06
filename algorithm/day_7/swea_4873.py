# 직접 push, pop 함수 만드는 것은 마지막 위치를 찾기도 쉽지가 않고
# pop해도 자료가 남아있어서 연산이 쉽지 않은 듯,.,.,.,.,.,

# def push(item, size):
#     global top
#     top += 1
#     if top == size:
#         return 0
#     else:
#         stack[top] = item
#         return 0

T = int(input())

for tc in range(1, T + 1):
    S = input()

    # size = 1000
    # stack = [0] * size
    # top = -1

    stack = [] # 스택 생성
    stack_len = 0

    for s in S: # 문자열 돌면서 일단 넣어
        stack.append(s)
        stack_len += 1
        # 스택의 길이가 2 이상이고, 마지막 두개의 값이 일치하는 동안 계속 지워봄
        while stack_len >= 2 and stack[-1] == stack[-2]:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                stack_len -= 2 # 스택 길이 줄이는 거 잊지 말자

    print(f'#{tc} {len(stack)}')
