import sys

sys.stdin = open("_파리퇴치.txt")

t = int(input())

for tc in range(1, t + 1) :
    n, m = map(int, input().split())