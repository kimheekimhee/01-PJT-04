from collections import deque
import sys

sys.stdin = open("_암호생성기.txt")


for testcase in range(10):
    t = int(input())
    nums = deque(list(map(int, input().split())))
    print(type(nums))
    i = 1

    while True:
        if i > 5:
            i = 1

        n = nums.popleft() - i
        if n <= 0:
            nums.append(0)
            break

        i += 1

    print('#', t * nums, end=' ')
