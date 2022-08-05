import sys

sys.stdin = open("_파리퇴치.txt")

test_case = int(input())
for _ in range(test_case):
    N, M = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(N)]
    
    
