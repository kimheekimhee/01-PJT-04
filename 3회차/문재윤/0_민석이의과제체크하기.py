import sys

sys.stdin = open("_민석이의과제체크하기.txt")

n = int(input())

for j in range(1,n+1):
    a ,b = map(int,input().split())
    list_ = list(range(1,a+1))
    list2 = list(map(int,input().split()))
    for i in list2:
        list_.remove(i)
    print('#',end="")
    print(j,end=' ')
    list_=[str(a) for a in list_]
    print(' '.join(list_))

