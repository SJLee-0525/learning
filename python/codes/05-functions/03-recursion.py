def factorial(n):
    # 종료 조건 (Base Case): n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n - 1) # 함수 내에서 자신의 함수를 다시 호출


# 팩토리얼 계산 예시
print(factorial(5))  # 120

# 자기 자신을 다시 호출할 때 n을 그대로 두면, 무한 순회하니 주의