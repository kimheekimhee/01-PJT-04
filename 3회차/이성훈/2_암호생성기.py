import sys
from collections import deque

sys.stdin = open("_암호생성기.txt")

for _ in range(10):

    T = int(input())

    N = deque(map(int, input().split()))

    N1 = list(range(1,6))

    while N[-1] > 0:
        for i in range(1,6):
            N.append(N.popleft()-i)
            if N[-1] <= 0 :
                break
            
    if N[-1] <= 0:
        N[-1] = 0
        print(f'#{T}',*N)