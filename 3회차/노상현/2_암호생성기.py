import sys

sys.stdin = open("_암호생성기.txt")


T = 10
for t in range(1, T+1):
    input()
    password = list(map(int, input().split()))
    i = 1
