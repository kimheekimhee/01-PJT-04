from collections import deque
import sys

sys.stdin = open("_암호생성기.txt")
from collections import deque

for test_case in range(10):
    T = int(input())
    number = deque(map(int, input().split()))

    while number[7] != 0:
        for a in range(1,6):
            N = number.popleft()
            if N-a>0:
                number.append(N-a)
            else :
                number.append(0)
                break
                

    print(f"#{T} {' '.join(map(str,number))}")



        



