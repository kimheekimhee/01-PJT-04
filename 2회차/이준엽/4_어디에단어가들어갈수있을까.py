t = int(input())
for _ in range(1,t+1):
    n, k = map(int,input().split())
    puzzle = [list(map(int,input().split())) for i in range(n)]
    psb = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[i][j] == 0:
                if cnt == k:
                    psb+=1
                    cnt = 0
                else:
                    cnt=0
            elif puzzle[i][j] == 1:
                cnt+=1
                if j == n-1 and cnt ==k:
                    psb+=1
                else:
                    pass
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[j][i] == 0:
                if cnt == k:
                    psb+=1
                    cnt = 0
                else:
                    cnt=0
            elif puzzle[j][i] == 1:
                cnt+=1
                if j == n-1 and cnt ==k:
                    psb+=1
                else:
                    pass
    print(f'#{_}',psb)