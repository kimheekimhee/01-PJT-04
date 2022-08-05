import sys
from collections import deque

sys.stdin = open("_암호생성기.txt")

for _ in range(10):
    n = int(input())
    nums = deque(list(map(int, input().split())))
    cnt = 1
    while True:
        if cnt == 6:
            cnt = 1
        nums[0] -= cnt
        if nums[0] <= 0:
            nums[0] = 0
            nums.rotate(-1)
            break
        else:
            cnt += 1
            nums.rotate(-1)
    print(f"#{n}", end=" ")
    print(*nums, sep=" ")