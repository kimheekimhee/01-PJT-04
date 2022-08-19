from pprint import pprint
import sys

sys.stdin = open("_파리퇴치.txt")

t = int(input())


for t in range(1,  t + 1):
    n, m = map(int, input().split())
    flys = [list(map(int, input().split())) for i in range(n)]
    #print(flys)

    max_sum = 0
    
    for r in range(n):
        for c in range(n):
            if c + (m - 1) < n and r + (m - 1) < n:
                sum = 0
                for fr in range(r, (r + (m))):    
                    for fc in range(c, (c + (m))):
                        sum += flys[fr][fc]
                #print(sum)
                if sum > max_sum:
                    max_sum = sum
    print(f'#{t} {max_sum}')


