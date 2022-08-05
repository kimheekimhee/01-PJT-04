import sys

sys.stdin = open("_파리퇴치.txt")



N = int(input())

for i in range(N):
    fly = list(map(int,input().split()))

for i in range(N):
    for j in range(N):
        print(fly[i][j])
