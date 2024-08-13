Q_size = 4
cQ = [0] * 4
front = rear = 0

# enQueue(1)
rear = (rear + 1) % Q_size
cQ[rear] = 1

# enQueue(2)
rear = (rear + 1) % Q_size
cQ[rear] = 2

# enQueue(3)
rear = (rear + 1) % Q_size
cQ[rear] = 3

# deQueue()
front = (front + 1) % Q_size
print(cQ[front])

# deQueue()
front = (front + 1) % Q_size
print(cQ[front])

# deQueue()
front = (front + 1) % Q_size
print(cQ[front])

# enQueue(10)
rear = (rear + 1) % Q_size
cQ[rear] = 10

# enQueue(20)
rear = (rear + 1) % Q_size
cQ[rear] = 20

print(cQ)