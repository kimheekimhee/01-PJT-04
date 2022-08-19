import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for t in range(T):

    N, M = map(int, input().split())

    N_space = [[0 for i in range(N)] for j in range(N)]

    for i in range(N):
        N_space[i] = list(map(int, input().split()))

    sum_list = []
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
                
            for m1 in range(M):
                for m2 in range(M):
                    sum += N_space[i+m1][j+m2]
            
            sum_list.append(sum)
    
    print(f'#{t+1}',max(sum_list))
                    

