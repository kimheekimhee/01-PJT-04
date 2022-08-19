import sys

sys.stdin = open("_암호생성기.txt")

# 5번이 한 사이클
# 0이거나, 0보다 작아지거나 -> 0 -> 끝

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