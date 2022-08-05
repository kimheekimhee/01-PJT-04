# N*N 크기의 단어퍼즐..
# 입력으로 단어 퍼즐 보드 모양
# k개의 길이를 갖는 단어가 들어갈 수 있는 빈칸의 갯수(딱맞아야함.)

import sys
sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())
for test_case in range(1,T+1):

    n,k = map(int,input().split())
    board = []
    for i in range(n):
        temp = list(map(int,input().split()))
        board.append(temp)
    # n, k = 8,3
    # board = [[1, 1, 0, 1, 0, 1, 1, 1],
    #          [0, 1, 0, 1, 0, 0, 0, 1],
    #          [1, 1, 1, 0, 0, 1, 0, 1],
    #          [0, 1, 0, 1, 0, 1, 1, 1],
    #          [0, 0, 0, 1, 0, 1, 0, 1],
    #          [1, 1, 1, 1, 1, 1, 0, 0],
    #          [0, 1, 0, 0, 0, 1, 0, 1],
    #          [1, 1, 1, 0, 1, 1, 1, 1]]

    word = 0
    for y in range(n):
        cnt_w = 0
        for x in range(n):
            if board[y][x] == 1:
                cnt_w += 1
            else : 
                if cnt_w == k:
                    word += 1
                # print(board[y],cnt_w)
                cnt_w = 0
        if cnt_w == k:
            # print(board[y],cnt_w)
            word += 1
            
    for x in range(n):
        rev_board = [board[y][x] for y in range(n)]
        # print(rev_board)
        cnt_h = 0
        for y in range(n):
            if rev_board[y] == 1:
                cnt_h += 1
            else : 
                # print(rev_board,cnt_h)
                if cnt_h == k:
                    word += 1
                cnt_h = 0
        if cnt_h == k:
            word += 1

    result = word
    print(f'#{test_case} ',result)

    