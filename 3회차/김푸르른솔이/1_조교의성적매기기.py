import sys

sys.stdin = open("_조교의성적매기기.txt")

n = int(input())

for _ in range(1, n+1):
    a, b = list(map(int, input().split()))
