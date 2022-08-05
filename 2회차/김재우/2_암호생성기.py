import sys

sys.stdin = open("_암호생성기.txt")

T = 10

for tc in range(1, T+1):
    tc_list = input()
    num = list(map(int, input().split()))
    minus = 1
    
    while True:
        
        if minus > 5:
            minus = 1
        
        num.append(num.pop(0) - minus)

        if num[7] <= 0:
            num[7] = 0
            break

        minus += 1
    
    print(f'#{tc}', end =' ')
    print(*num)