import sys

sys.stdin = open("./3회차/신윤식/_어디에단어가들어갈수있을까.txt")

T = int(input())

for t in range(1, T+1):
    N, K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    matrix_r = matrix
    matrix_l = matrix

    for row in range(N):
        i = 1
        for col in range(N):
            if matrix[row][col] == 0:
                i = 0
                continue
            elif matrix[row][col] == 1:
                matrix_r[row][col] = i
                i+=1
    
    count_r = 0

    for o in matrix_r:
        if max(o) <= K:
            count_r += o.count(K)


    for row in range(N):
        j = 1
        for col in range(N):
            if matrix[col][row] == 0:
                j = 0
                continue
            elif matrix[col][row] == 1:
                matrix_l[col][row] = j
                j+=1
    print(matrix_l)
    # count_l = 0
    
    # for u in matrix_l:
    #     if max(u) <= K:
    #         count_l += u.count(K)
    
    # print(count_r + count_l)
    
    
    # count = 0
    # a = 0

    # for row in range(N):
    #     for col in range(N-K+1):
    #         if matrix[row][col] == 1:
    #             if matrix[row][col+1] == 1:
    #                 a += 1
    #         if a == K-1:
    #             count += 1
    
    # print(count)
    #                 else:
    #                     a = False
    #                     break
    #             if a == True:

    #                 count+=1
    # print(count)