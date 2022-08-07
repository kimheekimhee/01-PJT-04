import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    cnt_r = 0
    cnt_c = 0

    for r in puzzle:
        cnt = 0
        for i in r:
            if i == 1:
                cnt += 1
            else:
                if cnt == K:
                    cnt_r += 1   
                cnt = 0
        if cnt == K:
            cnt_r += 1
            
            
    for c in range(N):
        cnt = 0
        for r in range(N):
            if puzzle[r][c] == 1:
                cnt += 1
            else:
                if cnt == K:
                    cnt_c += 1
                cnt = 0
        if cnt == K:
            cnt_r += 1
                
                
    print(f'#{tc} {cnt_c + cnt_r}')
