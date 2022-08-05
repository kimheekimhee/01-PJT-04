import sys

sys.stdin = open("_파리퇴치.txt")

t = int(input())

for i in range(t):
    n, m = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]

    