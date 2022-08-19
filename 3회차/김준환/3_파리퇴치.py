import sys
from pprint import pprint
sys.stdin = open("_파리퇴치.txt")

def Dead_Count(i,j):
    s = 0
    dead_lst = set()
    for col in range(i,i+m):
        for row in range(j,j+m):
            s += matrix[col][row]
            dead_lst.add(s)
    return s


t = int(input())
for test in range(t):
    result = set()
    n, m = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    
    for i in range(n-m+1):
        for j in range(n-m+1):
            result.add(Dead_Count(i,j))
    print(f'#{test+1} {max(result)}')