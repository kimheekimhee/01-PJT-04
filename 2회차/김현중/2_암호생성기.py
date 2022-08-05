import sys
from collections import deque
sys.stdin = open("_암호생성기.txt")
input = sys.stdin.readline


for _ in range(10):
    test_case = int(input())
    nums = deque(list(map(int, input().split())))
    while True:
        if nums[-1] == 0:
            break
        for i in range(1, 6):
            if nums[0] - i <= 0:
                nums[0] = 0
                nums.append(nums.popleft())
                break
            else:
                nums[0] = nums[0] - i
                nums.append(nums.popleft())
    print(f'#{test_case}',end=' ')
    print(*nums)