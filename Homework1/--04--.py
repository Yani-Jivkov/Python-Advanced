from collections import deque
dispenser = int(input())
queue = deque()
while True:
    name = input()
    if name == 'Start':
        break
    queue.append(name)
while True:
    commandr = input()
    if commandr == 'End':
        break
    commandr = commandr.split(' ')
    if commandr[0] == 'refill':
        dispenser += int(commandr[1])
    else:
        if int(commandr[0]) <= dispenser:
            print(f'{queue.popleft()} got water')
            dispenser -=  int(commandr[0])
        else:
            print(f'{queue.popleft()} must wait')
print(f'{dispenser} liters left')