import sys

sys.stdin = open("_암호생성기.txt")

T = 10
for tc in range(1, T+1):
    n = int(input())
    number = list(map(int, input().split()))
    m = 1 
 
    while True:
        change_num = number.pop(0) - m
        if change_num < 0: 
            change_num = 0
        number.append(change_num)
        if change_num == 0:
            break
        m += 1 
        if m > 5:                    
            m = 1
    result = ' '.join(str(s) for s in number)
    print(f'#{tc} {result}')
