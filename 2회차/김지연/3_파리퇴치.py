from pprint import pprint
# import sys

# sys.stdin = open("_파리퇴치.txt")

T = int(input())
N, M = map(int, input().split())
arr = []

for i in range(N):
    n = list(map(int, input().split()))
    arr.append(n)

pprint(arr)