import sys
from collections import deque

test_case = int(input())
pw = deque(map(int, input().split()))

while pw[-1] > 0:
    for i in range(1, 6):
        pw[0] = pw[0] - i
        pw.append(pw.popleft())
        
print('#{} {}'.format(test_case, pw, end = ' '))

sys.stdin = open("_암호생성기.txt")
