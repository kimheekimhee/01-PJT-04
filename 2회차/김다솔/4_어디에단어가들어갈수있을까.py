import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # print(matrix)
    
    fit = 0
    #행
    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[i][j] == 1:
                cnt += 1
                if cnt > 3:
                    cnt = 0