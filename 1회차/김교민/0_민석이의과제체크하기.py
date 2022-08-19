import sys

sys.stdin = open("_민석이의과제체크하기.txt")

t = int(input())

for case in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    list_ = []
    for i in range(1,n+1):
        if i not in p:
            list_.append(i)
    print(f'#{case+1}', *list_)