# 이거 맞나..?

def cal_B(input_B):
    temp_B = 0  # 결과값 저장할 변수
    oper_B = 1  # 진수 자릿수 별로 곱할 숫자
    for b in range(len(input_B) - 1, -1, -1): # 뒤에서부터 돌면서
        temp_B += input_B[b] * oper_B   # 자릿수에 맞는 숫자 곱해서 더하고
        oper_B *= 2                     # 진수 자릿수에 맞는 숫자 갱신
    result_B.append(temp_B) # 결과값 추가

def cal_C(input_C):
    temp_C = 0
    oper_C = 1
    for c in range(len(input_C) - 1, -1, -1):
        temp_C += input_C[c] * oper_C
        oper_C *= 3
    result_C.append(temp_C)

T = int(input())
for tc in range(1, T + 1):
    B = list(map(int, input())) # 2진수
    C = list(map(int, input())) # 3진수

    # 각각 바꿔본 결과 담을 리스트
    result_B = []
    result_C = []

    # 각각 원본 복제
    original_B = B[:]
    original_C = C[:]

    # 2진수 하나씩 바꿔보기
    for b in range(len(B) - 1, -1, -1):
        if B[b]: # B[b]가 1이면 0으로 바꾸고 함수 호출
            B[b] = 0
            cal_B(B)
        else:   # B[b]가 0이면 1으로 바꾸고 함수 호출
            B[b] = 1
            cal_B(B)
        B = original_B[:] # 계산 후에는 원본으로 바꿔놓기

    # 3진수 하나씩 바꿔보기
    for c in range(len(C) - 1, -1, -1):
        if C[c] == 0:
            C[c] = 1 # C[c]가 0이면 1으로 바꾸고 함수 호출
            cal_C(C)
            C[c] = 2 # C[c]가 0이면 2로도 바꿔보고 함수 호출
            cal_C(C)
        elif C[c] == 1:
            C[c] = 0 # C[c]가 1이면 0으로 바꾸고 함수 호출
            cal_C(C)
            C[c] = 2 # C[c]가 1이면 2로도 바꿔보고 함수 호출
            cal_C(C)
        elif C[c] == 2:
            C[c] = 0 # C[c]가 2이면 0으로 바꾸고 함수 호출
            cal_C(C)
            C[c] = 1 # C[c]가 2이면 1로도 바꿔보고 함수 호출
            cal_C(C)
        C = original_C[:] # 계산 후에는 원본으로 바꿔놓기

    for r in result_B: # 2진수 결과값 담은 리스트에서 하나 뽑아서
        if r in result_C: # 3진수 결과값에 값이 있는 애가 있다면
            result = r  # 결과 할당하고 중지
            break

    print(f'#{tc} {result}')

