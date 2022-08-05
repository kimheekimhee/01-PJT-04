import sys

sys.stdin = open("_파리퇴치.txt")

# 2차원 배열을 통해 접근

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    fly = [list(map(int,input().split())) for _ in range(N)]