import sys
sys.stdin = open("_암호생성기.txt")
T = 10
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))


    while numbers[-1] > 0 :
        for i in range(1, 6):
            num = numbers.pop(0)
            numbers.append(num - i)
            if numbers[-1] <= 0:
                numbers[-1] = 0
                break
    print(f'#{t}', *numbers)