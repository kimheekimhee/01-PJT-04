import sys

sys.stdin = open("_민석이의과제체크하기.txt")

t = int(input())

for _ in range(1,t+1):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    res = []
    for i in range(1,n+1):
        if i not in s:
            res.append(i)
    print(f'#{_}', *res)



        