# memo를 위한 배열을 할당하고, 모두 0으로 초기화 한다
# memo[0]은 0으로, memo[1]은 1로 초기화 한다. (피보나치 수의 특성)

def fibo_memo(n): # 메모이제이션
	global memo
	if n >= 2 and memo[n] == 0: # fibo(n)이 계산된 적이 없으면
		memo[n] = fibo_memo(n - 1) + fibo_memo(n - 2)
	return memo[n]

def fibo_1(n): # 재귀
	if n < 2:
		return n
	else:
		return fibo_1(n - 1) + fibo_1(n - 2)

def fibo_dp(n): # 피보나치 수 DP 적용 알고리즘
	f = [0] * (n + 1)
	f[0] = 0
	f[1] = 1
	for i in range(2, n + 1):
		f[i] = f[i - 1] + f[i - 2]
	return f[n]

n = 13

memo = [0] * (n + 1)
memo[0] = 0
memo[1] = 1


print(fibo_memo(n))
print(memo)
# print(fibo_1(n))
# print(fibo_dp(n))

