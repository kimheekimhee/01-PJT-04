import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for x in range(N)]
    result_cnt = 0
    for a in range(N):
        cnt = 0
        for b in range(N):
            if puzzle[a][b] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result_cnt += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt == K:
            result_cnt += 1

    for a in range(N):
        cnt = 0
        for b in range(N):  
            if puzzle[b][a] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result_cnt += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt == K:
            result_cnt += 1
    print(f'#{_ + 1} {result_cnt}')