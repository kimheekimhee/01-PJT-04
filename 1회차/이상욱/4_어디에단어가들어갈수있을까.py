import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    matrix=[list(map(int, input().split())) for _ in range(N)]
    result_X = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[i][j] == 1:
                cnt += 1
            elif matrix[i][j] == 0:
                if cnt == K:
                    result_X += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt == K:
            result_X += 1

    result_Y = 0
    for k in range(N):
        cnt = 0
        for l in range(N):
            if matrix[l][k] == 1:
                cnt += 1
            elif matrix[l][k] == 0:
                if cnt == K:
                    result_Y += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt == K:
            result_Y += 1
    print(f'#{t} {result_X + result_Y}')