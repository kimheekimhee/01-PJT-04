from collections import deque
import sys

sys.stdin = open("test.txt")

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
