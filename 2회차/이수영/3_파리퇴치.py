import sys

sys.stdin = open("_파리퇴치.txt")
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []
    
    for i in range(N-M):
        for j in range(N-M):
            sum_ = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
            sum_list.append(sum_)
    print(max(sum_list))
