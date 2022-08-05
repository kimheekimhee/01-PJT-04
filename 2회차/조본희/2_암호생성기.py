import sys

sys.stdin = open("_암호생성기.txt")

for test_case in range(1, 11):
    t = int(input())
    numbers = list(map(int, input().split()))
    subnum = 1
    while True:
        temp = numbers.pop(0)
        if temp - subnum <= 0:
            numbers.append(0)
            break
        numbers.append(temp - subnum)
        subnum += 1
        if subnum > 5:
            subnum = 1
    print(f'#{t} ', end='')
    print(*numbers, sep=' ')