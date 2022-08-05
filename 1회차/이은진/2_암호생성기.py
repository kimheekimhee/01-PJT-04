from asyncio import queues
import sys

# sys.stdin = open("_암호생성기.txt")

t = int(input())
origin = list(map(int, input().split(' ')))

# 큐로 바꾸는 방법 까먹음
for a in range(1, min(origin)):
    origin = origin.append(origin.leftpop()-a)
    if origin.leftpop() == 0:
        break
    # origin[0] 빼는 메서드 이름..

