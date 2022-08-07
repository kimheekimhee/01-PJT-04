'''
못 풀겠음
'''
# import sys
import copy
# sys.stdin = open("./3회차/신윤식/_어디에단어가들어갈수있을까.txt")

T = int(input())

for t in range(1, T+1):
    N, K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    matrix_r = copy.deepcopy(matrix)
    matrix_l = copy.deepcopy(matrix)
    

    
    # 행
    for row_1 in range(N):
        i = 1
        for col_1 in range(N):
            if matrix_r[row_1][col_1] == 0:
                if i != 1:
                    i = 1
                else:
                    continue
            elif matrix_r[row_1][col_1] == 1:
                matrix_r[row_1][col_1] = i
                i+=1

    count_r = 0
    
    for a in range(N):
        for b in range(N-1):
            if matrix_r[a][b] == K:
                if matrix_r[a][b+1] == 0:
                    count_r += 1
                else:
                    continue
        if matrix_r[a][-1] == K:
            count_r += 1
    
    print(count_r)



    # 열
    
    # lst2 = []

    # for a in range(N):
    #     lst = []
    #     for b in range(N):
    #         lst.append(matrix_l[b][a])
    #     lst2.append(lst)
    
    # for row_2 in range(N):
    #     j = 1
    #     for col_2 in range(N):
    #         if lst2[row_2][col_2] == 0:
    #             if j != 1:
    #                 j = 1
    #             else:
    #                 continue
    #         elif lst2[row_2][col_2] == 1:
    #             lst2[row_2][col_2] = j
    #             j+=1
    
    # count_l = 0

    # for y in matrix_l:
    #     if max(y) == K:
    #         count_l += y.count(K)   


    # for row in range(N):
    #     j = 1
    #     for col in range(N):
    #         if matrix[col][row] == 0:
    #             j = 0
    #             continue
    #         elif matrix[col][row] == 1:
    #             matrix_l[col][row] = j
    #             j+=1
    # print(matrix_l)
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