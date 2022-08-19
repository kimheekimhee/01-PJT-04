import sys
sys.stdin = open("_암호생성기.txt")

T = 10 
for i in range(T):
    N = int(input())
    numbers = list(map(int,input().split()))
    j = 1 
    while 1:
        if j > 5:
            j = 1
        num = numbers.pop(0) - j
        if num > 0:
            numbers.append(num)
            j += 1
        else:
            numbers.append(0)
            break
    print(f'#{i+1}',end=' ')
    print(*numbers)

    