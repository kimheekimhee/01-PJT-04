import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for i in range(T):
    N, K = map(int,input().split())
    n = list(map(int,input().split()))
    res = []
    for j in range(1,N+1):        
        if j not in n:
            res.append(j)
    print(f'#{i+1}', *res)
