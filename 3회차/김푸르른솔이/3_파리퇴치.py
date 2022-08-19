import sys

sys.stdin = open("_파리퇴치.txt")


n = int(input())
matrix = []
a, b = map(int, input().split())

for _ in range(1, n + 1):
    line = list(map(int, input().split()))
