import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    #가로 돌기
    for i in range(n):
        row = 0
        for j in range(n):
            if board[i][j] == 1:
                row += 1
            else:
                row = 0

        if row == k:
            result += 1
    #세로 돌기
    for i in range(n):
        column = 0
        for j in range(n):
            #단어가 없으면
            if board[j][i] == 1:
                column += 1
            else:
                #빈칸의 개수가 k랑 같으면
                if column == k:
                    result += 1
                    column = 0
                else:
                    column = 0
    
    print(f"#{tc} {result}")
                