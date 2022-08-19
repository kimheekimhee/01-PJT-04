import sys

sys.stdin = open("_파리퇴치.txt")


T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())