import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for z in range(T):
    N,M=map(int,input().split())
    board = []
    for y in range(N):
        line = list(map(int, input().split()))
        board.append(line)
    fly = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0
            for c in range(M):
                for d in range(M):
                    if i + c in range(N) and j + d in range(N):
                        catch += board[i + c][j + d]
            fly.append(catch)
    print(f'#{z+1} {max(fly)}') 