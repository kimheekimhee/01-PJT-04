import sys
from pprint import pprint
sys.stdin = open("_파리퇴치.txt")

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    kill_list = []
    move = n - m +1
    A = n - m + 1
    for a in range(A):
        kill_sum = 0
        for i in range(a,m+a):
            for j in range(a,m+a):
                kill_sum += board[i][j]
        kill_list.append(kill_sum)
    print(f'#{t} {max(kill_list)}')