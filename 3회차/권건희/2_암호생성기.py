import sys

sys.stdin = open("_암호생성기.txt")
from collections import deque
for _ in range(10):
    a=input()
    T=(map(int,input().split()))
    queue=deque(T)
    cnt=0
    while(queue[0]!=0):
        cnt+=1
        if queue[0]-cnt>0:
            s=queue.popleft()
            queue.append(s-cnt)
        else: 
            queue.popleft()
            queue.append(0)
            break   
    print(f"#{a} {queue}")