import sys

sys.stdin = open("_파리퇴치.txt")
t = int(input())
for _ in range(1,t+1):
    n, m = map(int, input().split())
    for _ in range(n):
        borad = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            print(borad[i][j])