from itertools import tee
import sys

sys.stdin = open("_암호생성기.txt")
t = 10
for i in range(1,t+1):
    n = int(input())
    b = list(map(int, input().split()))
