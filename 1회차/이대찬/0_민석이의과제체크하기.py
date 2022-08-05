import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for i in range(1,T+1):
    N,K = map(int,input().split())
    lst = list(map(int,input().split()))
    print(f'#{i}',end=' ')
    for n in range(1,N+1):
        if n not in lst:
            print(f'{n}',end=' ')
    print()
            
        