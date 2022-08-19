import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    paris = [list(map(int, input().split())) for _ in range(N)]
    max = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_ = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    sum_ += paris[x][y]
            if sum_ > max:
                max = sum_

    print('#%d' %t, max)