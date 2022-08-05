import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]