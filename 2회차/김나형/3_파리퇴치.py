from re import L
import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input(). split())

    a = [list(map(int, input().split())) for _ in range(N)]
    score_li = []
    score = 0
    x = 0
    y = 0

    while True:    
        for i in range(x, x + M):
            for j in range(y, y + M):
                score += a[i][j]
        score_li.append(score)
        y += 1
        score = 0

        if y + M > N:
            x += 1
            y = 0
        if x + M > N:
            break
        
    print(f'#{tc} {max(score_li)}')

        