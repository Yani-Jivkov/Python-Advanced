from collections import deque
names = input().split()
turn = int(input())
queue = deque(names)
turns = 0

while len(queue) > 1:
    helper = queue.popleft()
    turns += 1
    if turns % turn == 0:
        print(f'Removed {helper}')
    else:
        queue.append(helper)
print(f'Last is {queue.popleft()}')
