# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYJCO4t6cCMDFASv&contestProbId=AV14uWl6AF0CFAYD&probBoxId=AYJCPZjKcDYDFASv&type=PROBLEM&problemBoxTitle=2%EC%A3%BC%EC%B0%A8&problemBoxCnt=6

import sys

sys.stdin = open("_암호생성기.txt")

T = 10

for t in range(1, 10 + 1):
    tc = int(input())
    queue = list(map(int, input().split()))
    # print(queue[7])

    while True:
        for i in range(1, 6):
            queue[0] -= i
            queue.append(queue.pop(0))
            if queue[-1] <= 0:
                queue[-1] = 0
                break

    print(f'#{t} {queue}')

# 0보다 작은 수가 나올 경우 멈추고 0으로 값을 고정하는 걸 어떻게 하는지 모르겠다...





