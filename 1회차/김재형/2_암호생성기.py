import sys

sys.stdin = open("_암호생성기.txt")
# 1
# 9550 9556 9550 9553 9558 9551 9551 9551
for i in range(10):
    T = int(input())
    num = list(map(int, input().split()))

    # pop하고 append를 적절하게 사용해보자
    while num[0] > 5:
        for i in range(1,6):
            p = num.pop(0)
            num.append(p-i)
            # print(num)
        if p-i < 0:
            num.pop()
            num.append(0)
            print(num)
            break