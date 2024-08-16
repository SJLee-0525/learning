# def f(i, V, K):
#     global arr
#     if i == V:
#         print(arr[:K])
#     else:
#         for j in range(i, V):
#             arr[i], arr[j] = arr[j], arr[i]
#             f(i + 1, V, K)
#             arr[i], arr[j] = arr[j], arr[i]
#

# arr = list(range(5))
# f(0, len(arr), 3)

def ff(i, V):
    if i == V:
        result = []
        for j in range(V):
            if b[j]:
                result.append(arr2[j])
        print(result)
    else:
        b[i] = 1
        ff(i + 1, V)
        b[i] = 0
        ff(i + 1, V)

arr2 = list(range(5))
b = [0] * 5
ff(0, len(b))