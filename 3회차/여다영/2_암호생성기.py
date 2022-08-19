import sys
from collections import deque

sys.stdin = open("_암호생성기.txt")

for _ in range(10):
    T = int(input())

    numbers = list(map(int, input().split()))
    queue = deque(numbers)
    
    i = 1
    while True:
        if i == 6:
            i = 1

        temp = queue.popleft() - i
        if temp <= 0:
            queue.append(0)
            break
        else:
            queue.append(temp)

        i += 1
    
    print(f'#{T}', *queue)