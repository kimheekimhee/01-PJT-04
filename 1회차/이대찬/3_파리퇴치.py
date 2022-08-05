import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
result =[]
for i in range(1,T+1):
    N,M = map(int,input().split())
    matrix = list(list(map(int,input().split())) for _ in range(N))
    
    for R in range(0,N-M+1):
        for C in range(0,N-M+1):
            sum_ = 0
            for r in range(M):
                for c in range(M):
                    sum_ += matrix[r+R][c+C]
                 
            result.append(sum_)
            
            
    print(f'#{i} {max(result)}')
     
 


            