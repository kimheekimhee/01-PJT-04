import sys

sys.stdin = open("_암호생성기.txt")

for i in range(10):
    T = int(input())
    pass_ = list(map(int, input().split()))
  
    i = 1
    # for i in range(5):
    while pass_[7] > 0:
        pass_[0] = pass_[0] - (i)
        pass_.append(pass_[0])
        pass_.pop(0)
        i += 1
        if i == 6:
            i = 1

    if pass_[7] <= 0:
        pass_[7] = 0
    print('#{}'.format(T), *pass_)