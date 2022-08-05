import sys

sys.stdin = open("_암호생성기.txt")

T = 10

for tc in range(T):
    tc_list = input()
    num = list(map(int, input().split()))
    minus = 1
    while num[7] != 0:
        if minus > 5:
            minus = 1
        
        if num.pop(0) < 0:
            num.pop = 0
            break
        
        num.append(num.pop(0)-minus)

        minus += 1

        if num < 0:
            num[7] = 0 

    
    print(num)