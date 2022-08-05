import sys
from collections import deque

sys.stdin = open("_암호생성기.txt")

for _ in range(10):
    n = int(input())
    # rotate를 사용하기 위한 deque로 선언
    nums = deque(list(map(int, input().split())))
    # 얼마씩 빼기 위한 변수
    cnt = 1
    while True:
        # 6이상은 빼지 않으므로 6이면 1로 전환
        if cnt == 6:
            cnt = 1
        nums[0] -= cnt
        # 맨앞이 0이하면 0으로 설정후 뒤로 보내기
        if nums[0] <= 0:
            nums[0] = 0
            nums.rotate(-1)
            break
        else:
            cnt += 1
            nums.rotate(-1)
    print(f"#{n}", end=" ")
    print(*nums, sep=" ")