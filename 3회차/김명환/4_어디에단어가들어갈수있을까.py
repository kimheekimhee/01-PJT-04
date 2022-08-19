import sys
sys.stdin = open("_어디에단어가들어갈수있을까.txt")
T = int(input())
for i in range(T):
    N, K = map(int,input().split())
    num_list = []
    total_cnt = 0
    for j in range(N):
        num_list.append(list(map(int,input().split())))
        
    for x in range(N):
        cnt = 0 
        for y in range(N):
            if num_list[x][y] == 0:
                if cnt == K:
                    total_cnt += 1
                cnt = 0
            else: 
                cnt += 1
        if cnt == K:
            total_cnt += 1 
            
    for y in range(N):
        cnt = 0 
        for x in range(N):
            if num_list[x][y] == 0:
                if cnt == K:
                    total_cnt += 1
                cnt = 0
            else: 
                cnt += 1
        if cnt == K:
            total_cnt += 1 
            
    print(f'#{i+1} {total_cnt}') 