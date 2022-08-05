# import sys

# sys.stdin = open("_파리퇴치.txt")

# for num in range(1, int(input()) + 1) :
n, m = map(int, input().split())

flys = [list(map(int, (input().split()))) for _ in range(n)]

print(flys)
