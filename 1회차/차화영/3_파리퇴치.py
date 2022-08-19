from pprint import pprint
import sys

sys.stdin = open("_파리퇴치.txt")
T = int(input())
matrix = []
for tc in range(1, T+1):
    n, m = map(int, input().split())
    for _ in range(n):
        list_ = list(input().split())
        matrix.append(list_)
    