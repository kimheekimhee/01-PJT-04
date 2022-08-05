import sys
from turtle import pu

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [input().split() for _ in range(N)]        # 1 == 빈칸, 0 == 검은칸
    puzzle_row = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            puzzle_row[i][j] = puzzle[j][i]
    cnt = 0
    for row in puzzle:
        cnt += ''.join(row).split('0').count('1'*K)
    for row in puzzle_row:
        cnt += ''.join(row).split('0').count('1'*K)
    print(f'#{test_case} {cnt}')