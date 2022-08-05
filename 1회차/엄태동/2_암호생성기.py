import sys

sys.stdin = open("_암호생성기.txt")
from collections import deque
for i in range(10):
    testcase = int(input())
    List=deque(input().split())
    ForBreak=False
    while 1:
        for i in range(1,6):
            if int(List[0])-i <=0:
                num=0
                List.append(str(num))
                ForBreak=True
                List.popleft()
                break
            else:
                List.append(str(int(List[0])-i))

            List.popleft()