import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())
result =[]
for i in range(1,2):
    N,K = map(int,input().split())
    matrix = list(list(map(int,input().split())) for _ in range(N))
    sum_ = 0
    
    for r in range(N):
        cnt = 0
        for c in range(N):
            if matrix[r][c] == 1:
                cnt +=1
                if cnt > K:
                    cnt =1 
            elif matrix[r][c] == 0 and matrix[r][c-1] ==1 and cnt ==K:
                sum_ +=1
                cnt = 0
            else:
                continue
                
            if cnt == K and c == N-1:
                sum_ +=1
 
    print(f'#{i} {sum_}')
     