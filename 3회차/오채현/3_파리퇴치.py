import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for testcase in range(1, T + 1):
    # for testcase in range(1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    maxT = 0

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            total = 0
            for k in range(m):
                total += sum(matrix[i+k][j:j+m])
                if total > maxT:
                    maxT = total
    print(f'#{testcase} {maxT}')
