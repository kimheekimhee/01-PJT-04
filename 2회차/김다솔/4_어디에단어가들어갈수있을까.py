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
        r_cnt = 0
        for j in range(N):
            if matrix[i][j] == 0: 
                if r_cnt == K:
                    fit += 1
                r_cnt = 0 # 초기화
            elif r_cnt > K:
                r_cnt = 0
            r_cnt += matrix[i][j]
        if r_cnt == K:
            fit += 1
    
    for i in range(N):
        c_cnt = 0
        for j in range(N):
            if matrix[j][i] == 0:
                if c_cnt == K:
                    fit += 1
                c_cnt = 0 
            elif c_cnt > K:
                c_cnt = 0
            c_cnt += matrix[j][i]
        if c_cnt == K:
            fit += 1

    print(f'#{tc} {fit}')
            

        
