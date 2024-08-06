# 함수형
def my_push(item, size):
	global top
	top += 1
	if top == size:
		return 0
	else:
		stack1[top] = item
		return 0

def my_pop():
	global top
	if top < 0:
		return 0
	else:
		top -= 1
		return stack1[top + 1]

size = 3
stack1 = [0] * size
top = - 1

for num in range(1, 4):
	my_push(num, size)

print(my_pop())
print(my_pop())
print(my_pop())