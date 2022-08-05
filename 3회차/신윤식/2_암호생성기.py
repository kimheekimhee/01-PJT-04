import sys
from collections import deque

sys.stdin = open("./3회차/신윤식/_암호생성기.txt")

for _ in range(10):
    T = int(input())
    lst = map(int,input().split())
    queue = deque(lst)
    
    while queue[-1] != 0:
        for j in range(1,6):
            queue.append(queue.popleft() - j)
            if queue[-1] <= 0:
                queue[-1] = 0
                print(f'#{T}', end=' ')
                print(' '.join(map(str,queue)))
                break