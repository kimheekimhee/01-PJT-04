import sys
from collections import deque

sys.stdin = open("_암호생성기.txt")
count = 1
for _ in range(10):
    n = int(input())
    a = map(int, input().split())
    n_list = deque(a)

    while True:
        tmp = n_list.popleft()-count
        if tmp < 0 or tmp == 0:
            n_list.append(0)
            count = 1
            break
        elif tmp > 0:
            n_list.append(tmp)
            count += 1
        if count == 6:
            count = 1
    print(f'#{n}',end=' ')
    for i in n_list:
        print(i,end=' ')
    print()

