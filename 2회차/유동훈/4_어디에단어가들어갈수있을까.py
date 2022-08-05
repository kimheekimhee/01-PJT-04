import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())


for i in range(1, T+1):
    matrix = []
    N, K = map(int, input().split())
    for j in range(N):
        matrix.append(list(map(int, input().split())))

    cnt = 0
    white = 0
    for k in range(N):
        white = 0
        for l in range(N):
            if matrix[k][l] == 1:
                white += 1
                if l == N-1:
                    if white == K:
                        cnt+=1
            elif matrix[k][l] == 0:
                if white == K:
                    cnt+=1
                white = 0

    white = 0
    for k in range(N):
        white = 0
        for l in range(N):
            if matrix[l][k] == 1:
                white += 1
                if l == N-1:
                    if white == K:
                        cnt+=1
            elif matrix[l][k] == 0:
                if white == K:
                    cnt+=1
                white = 0
                    
    print(f'#{i} {cnt}')