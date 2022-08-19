import sys

sys.stdin = open("_암호생성기.txt")

t = int(input())
card = []
for _ in range(t):
    nums = list(map(int,input().split()))

    for i in range(len(nums)):
        print(nums, len(nums))
#하다말았어요
