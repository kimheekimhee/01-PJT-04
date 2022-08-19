import sys

sys.stdin = open("_암호생성기.txt")

from collections import deque

for i in range(10) :
    t = int(input())

    numlist = deque(list(map(int, input().split())))

    # print(numlist[0])
   
    while True :
        its = True
        for i in range(1, 6) :
            num = numlist[0] - i
            numlist.popleft()
            numlist.append(num)
            if num <= 0 :
                numlist[-1] = 0
                its = False
                break

        if its == False :
            print(f'#{t} ', end = '')
            print(*numlist)
            break
