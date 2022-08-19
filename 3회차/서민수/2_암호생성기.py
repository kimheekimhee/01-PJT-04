import sys

sys.stdin = open("_암호생성기.txt")

# 맨 앞에 있는 숫자가 -1,-2,-3,-4,-5 1사이클을 돌면서 
# 뒤로 움직이고 0이 되는순간 종료

T = 10
for t in range(1, T+1):
    tc = int(input())
    queue = list(map(int, input().split()))

    i = 1
    while True:
        if i > 5:
            i = 1
        t = queue.pop(0) - i
        if t <= 0:
            queue.append(0)
            break
        queue.append(t)
        i += 1

    print("#{} {} {} {} {} {} {} {} {}".format(tc, *queue))