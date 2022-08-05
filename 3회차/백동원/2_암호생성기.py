import sys
from collections import deque

sys.stdin = open("_암호생성기.txt")

for a in range(10):
    b = int(input())
    cnt = 1
    numbers = deque(list(map(int, input().split())))
    while True:
        popnumber = numbers.popleft()
        if popnumber - cnt <= 0:
            popnumber = 0
            numbers.append(popnumber)
            break
        else:
            numbers.append(popnumber - cnt)
            cnt += 1
            if cnt == 6:
                cnt = 1
    print(f'#{b}', end = ' ')
    print(*numbers)