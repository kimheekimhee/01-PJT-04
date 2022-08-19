import sys

sys.stdin = open("_파리퇴치.txt")



T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    n = M -1
    max_v = 0

    for i in range(N-n):
        for j in range(N-n):
            sum_v = 0
            for di in range(M):
                for dj in range(M):
                    sum_v += arr[i+di][j+dj]

            if sum_v > max_v:
                max_v = sum_v
        
    print('{} {}'.format(tc,max_v))

    



