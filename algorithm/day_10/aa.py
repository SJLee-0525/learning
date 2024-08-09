def f(idx, N):
	if idx == N:
		print(arr)
	else:
		for i in range(idx, N):
			arr[idx], arr[i] = arr[i], arr[idx] # 순서를 바꾸고
			f(idx + 1, N)
			arr[idx], arr[i] = arr[i], arr[idx] # 원상 복구

arr = [1, 2, 3]
N = 3
f(0, N)