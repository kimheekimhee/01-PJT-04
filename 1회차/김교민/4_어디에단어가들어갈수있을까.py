import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

t = int(input())

for case in range(1, t+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    
    re = 0
    
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == n-1:
                if cnt == k:
                    re += 1
                if puzzle[i][j] == 0:
                    cnt = 0
        
    
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == n-1:
                if cnt == k:
                    re += 1
                if puzzle[j][i] == 0:
                    cnt = 0
    print(f'#{case} {re}')