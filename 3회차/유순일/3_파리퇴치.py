import sys

sys.stdin = open("_파리퇴치.txt")

# N x N의 배열의 각 칸에 있는 파리를
# M x M의 크기의 파리채로 잡겠다는 문제.

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
# 5 = N, 2 = M
# 1 3 3 6 7         -> 파리가 한칸 당 1마리, 3마리, 3마리 ... 있다는 뜻.
# 8 13 9 12 8
# 4 16 11 12 6
# 2 4 1 23 2
# 9 13 4 7 3
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(N):          # 열순회
        for j in range(N):      # 행순회
            