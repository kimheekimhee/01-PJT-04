import sys

sys.stdin = open("_암호생성기.txt")

# deque
for _ in range(1, 11):
    n = int(input())
    list_ = list(map(int, input().split()))
    # print(list_)
    res = True
    k = 1
    while res:
        if k > 5:
            k = 1
        new_num = list_[0] - k
        k += 1
        # 종료 조건
        if new_num <= 0:
            new_num = 0
            res = False
        # list_뒤로 이동
        # 1. list_[0]을 pop
        # 2. list_.append(new_num)
        list_.remove(list_[0])
        list_.append(new_num)
        # print(list_)
    print('#', _, ' ', sep='', end='')
    for i in list_:
        print(i, end=' ')
    print()