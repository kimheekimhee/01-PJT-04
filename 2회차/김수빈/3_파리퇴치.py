import sys
sys.stdin = open("_파리퇴치.txt")

T = int(input())

for _ in range(1, T + 1):
    N, M = map(int, input().split())
    fly = []
    for i in range(N):
        fly.append(list(map(int, input().split())))
        score = []
        for j in range(M):
            score.append(fly[i][j])
            i += 1