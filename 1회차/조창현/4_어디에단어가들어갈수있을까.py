from pprint import pprint
import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

t = int(input())

for t in range(1, t + 1):
    n, k = map(int, input().split())

    mat = [list(map(str, input().split())) for _ in range(n)]
    #pprint(mat)
    trans_mat = [[0] * n for _ in range(n)]
    #pprint(trans_mat)
    word = []
    for i in range(k):
        word.append('1')
    #print(word)
    word_ans = ''.join(word)
    #print(word_ans)
    posi_cnt = 0

    for r in range(n):
        hori_list = ''.join(mat[r]).split('0')
        #print(hori_list)
        if str(word_ans) in hori_list:
            posi_cnt += hori_list.count(str(word_ans))
    #print(posi_cnt)

    for r in range(n):
        for c in range(n):
            trans_mat[c][r] = mat[r][c]
    #pprint(trans_mat)

    for r in range(n):
        hori_list = ''.join(trans_mat[r]).split('0')
        #print(hori_list)
        if str(word_ans) in hori_list:
            posi_cnt += hori_list.count(str(word_ans))
    print(f'#{t} {posi_cnt}')






    # for r in range(n):
    #     for c in range(n):
    #         if c + (k - 1) < n:
    #             posi_block = 0
    #             for fc in range(c, (c + (k))): 
    #                 print(r, fc)    
    #                 if mat[r][fc] == 1:
    #                     posi_block += 1
    #                     print(posi_block)
    #                     if posi_block == 3 and fc == n - 1:
    #                         posi_cnt += 1
    #                         print(f'cnt {posi_cnt}')
    #                     elif posi_block == 3 and mat[r][fc + 1] == 0:
    #                         posi_cnt += 1
    #                         print(f'cnt {posi_cnt}')
    #                     elif posi_block == 3 and mat[r][fc + 1] == 1:
    #                         break
    #                 elif mat[r][fc] == 0:
    #                     posi_block = 0
    #                     print(posi_block)

    # for r in range(n):
    #     posi_block = 0
    #     for c in range(n): 
    #         print(r, c)    
    #         if mat[r][c] == 1:
    #             posi_block += 1
    #             print(posi_block)
    #             if posi_block == 3 and c == n - 1:
    #                 posi_cnt += 1
    #                 print(f'cnt {posi_cnt}')
    #             elif posi_block == 3 and mat[r][c + 1] == 0:
    #                 posi_cnt += 1
    #                 print(f'cnt {posi_cnt}')
    #             elif posi_block == 3 and mat[r][c + 1] == 1:
    #                 posi_block = 0
    #         elif mat[r][c] == 0:
    #             posi_block = 0
    #             print(posi_block)


    # for r in range(n):
    #     for c in range(n):
    #         trans_mat[c][r] = mat[r][c]
    # pprint(trans_mat)

    # for r in range(n):
    #     posi_block = 0
    #     for c in range(n): 
    #         print(r, c)    
    #         if trans_mat[r][c] == 1:
    #             posi_block += 1
    #             print(posi_block)
    #             if posi_block == 3 and c == n - 1:
    #                 posi_cnt += 1
    #                 print(f'cnt {posi_cnt}')
    #             elif posi_block == 3 and trans_mat[r][c + 1] == 0:
    #                 posi_cnt += 1
    #                 print(f'cnt {posi_cnt}')
    #             elif posi_block == 3 and trans_mat[r][c + 1] == 1:
    #                 posi_block = 0
    #         elif trans_mat[r][c] == 0:
    #             posi_block = 0
    #             print(posi_block)
    # print(f'#{t} {posi_cnt}')