import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # print(matrix)
    answer = []
    for r in range(N - 1):
        for c in range(N):
            # 위쪽 행을 슬라이스한 결과
            up = sum(matrix[r][c:c + M])
            # 아래쪽 행을 슬라이스한 결과 
            down = sum(matrix[r + 1][c:c + M])
            answer.append(up+down)
    print(max(answer))
        