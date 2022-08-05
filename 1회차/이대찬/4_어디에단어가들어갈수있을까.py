import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())
result =[]
for i in range(1,T+1):
    N,K = map(int,input().split())
    matrix = list(list(map(int,input().split())) for _ in range(N))
    sum_ = 0
    
    for r in range(N):
        cnt_r = 0
        cnt_c = 0
        for c in range(N):
            if matrix[r][c] == 1:
                cnt_r +=1 
                if cnt_r == K and c== N-1:
                    sum_ += 1
            else:
                if cnt_r == K:
                    sum_ += 1
                    cnt_r = 0
                else:
                    cnt_r = 0
          
            if matrix[c][r] == 1:
                cnt_c +=1
                if cnt_c == K and c== N-1:
                    sum_ += 1
            else:
                if cnt_c == K:
                    sum_ += 1
                    cnt_c = 0
                else:
                    cnt_c = 0
                    
        
    print(f'#{i} {sum_}')
    