import sys

sys.stdin = open("_파리퇴치.txt")

from pprint import pprint

T = int(input())

for t in range(1, T+1):
    sumscore = 0
    n, m = list(map(int, input().split()))

    matrix = [list(map(int, input().split())) for _ in range(n)]

    for i in range(m):
        for j in range(m):
            sumscore += matrix[i][j]
    
    print(f'#{t} {sumscore}')