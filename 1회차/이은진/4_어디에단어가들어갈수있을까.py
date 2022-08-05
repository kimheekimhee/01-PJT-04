import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

for t in range(1, int(input())+1):
    x, y = map(int, input().split())
    board = []
    for _ in range(int(input())):
        board.append(list(map(int, input().split())))
        h_cnt, v_cnt = 0, 0
        for i in range(x):
            h_len, v_len = 0, 0
            for j in range(x):
                # 가로
                if board[i][j] == 1:
                    h_len += 1
                    if h_len == y:
                        h_cnt += 1
                elif board[i][j] == 0:
                    h_len = 0
                # 세로
                elif board[j][i] == 1:
                    v_len += 1
                    if h_len == y:
                        h_cnt += 1
                elif board[j][i] == 0:
                    h_len = 0
    print(f'#{t} {h_cnt + v_cnt}')