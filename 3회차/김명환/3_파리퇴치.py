import sys
sys.stdin = open("_파리퇴치.txt")

# 가장 왼쪽 위의 항 기준 5 x 5 일때 4x4 만 검사.

T = int(input())
for i in range(T):
    N, M = map(int,input().split())
    max = 0
    fly_list = []
    for j in range(N):
        fly_list.append(list(map(int,input().split())))
       
    for kx in range(N-M+1):
        for ky in range(N-M+1):
            sum = 0
            for kx2 in range(M):
                for ky2 in range(M):
                    sum += fly_list[kx+kx2][ky+ky2]
                if sum > max:
                    max = sum 
    print(f'#{i+1} {max}')



