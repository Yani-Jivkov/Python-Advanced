from collections import deque
queue = deque()
while True:
    data = input()
    if data == 'End':
        break
    elif data == 'Paid':
        for i in range(len(queue)):
            print(queue.popleft())
    else:
        queue.append(data)
print(f'{len(queue)} people remaining.')