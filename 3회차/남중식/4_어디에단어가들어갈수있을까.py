import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    grid = [[0 for y in range(N)] for x in range(N)]
    
    for j in range(N):
        grid[j] = list(map(int, input().split()))
        
    count_pos = 0
    
    for y in range(N):
        count_for_K = 0
        for x in range(N):
            if grid[y][x] == 1:
                count_for_K += 1
            if grid[y][x] == 0 or x == N-1:
                if count_for_K == K:
                    count_pos += 1  
                count_for_K = 0
                
    
    new_grid = [[0 for y in range(N)] for x in range(N)]
    
    for a in range(N):
        for b in range(N):
            new_grid[a][b] = grid[b][a]
                
    for y in range(N):
        count_for_K = 0
        for x in range(N):
            if new_grid[y][x] == 1:
                count_for_K += 1
            if new_grid[y][x] == 0 or x == N-1:
                if count_for_K == K:
                    count_pos += 1
                count_for_K = 0
    
    print(f'#{i+1}', count_pos)
    