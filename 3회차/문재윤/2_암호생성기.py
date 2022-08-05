import sys

sys.stdin = open("_암호생성기.txt")

for g in range(10):
        n = input()
        list_ = list(map(int,input().split()))
        while list_[7] != 0:
            for i in range(1,6):
                p = list_.pop(0)
                s = p -i
                if s < 0:
                    s = 0
                list_.insert(len(list_),s )
                if list_[7] == 0:
                    break
        print(f'#{n}',end=' ')
        list_=[str(a) for a in list_]
        print(' '.join(list_))