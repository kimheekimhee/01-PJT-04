import sys
from collections import deque

sys.stdin = open("_암호생성기.txt")

for s in range(10):
    n = int(input())
    number = list(map(int,input().split()))
    number = deque(number)
    while True:
        for i in range(len(number)):
            number[0] -= i
            number.append(number.popleft)    
            if number[-1] == 0:
                s = 'stop'
                print('#{}'.format(n),number)
                break
        if s =='stop':
            break
