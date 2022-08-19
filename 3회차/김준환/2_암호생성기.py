# import sys

# sys.stdin = open("_암호생성기.txt")
from collections import deque

for _ in range(10):
    t = int(input())
    num_lst = list(map(int,input().split()))
    # print(num_lst)
    # print(num_lst[0])
    breaker = False
    memory_lst = []
    while breaker == False:
        for idx in range(8):
            if num_lst[idx] < 120:
                breaker = True
                break
            else:
                num_lst[idx] -= 120
        if breaker == True:
            break
        memory_lst = num_lst
    num_deq = deque(memory_lst)
    breaker = False
    while True:
        for i in range(1,6):

            num_deq.append(deque.popleft(num_deq)-i)
            if num_deq[-1] <= 0:
                num_deq[-1]=0
                breaker = True
                break
        if breaker == True:
            break
    print(f'#{t} ',end='')
    for number in num_deq:
        print(number, end = ' ')
    print()