import sys

sys.stdin = open("./3회차/신윤식/_민석이의과제체크하기.txt")

T = int(input())

for _ in range(1, T+1):

    ans = []
    N, K = map(int,input().split())
    lst = list(map(int,input().split()))

    for i in range(1, N+1):
        if i not in lst:
            ans.append(i)
    
    print(f'#{_}', end=' ')
    for j in ans:
        print(j, end = ' ')
    print()