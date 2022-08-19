import sys

sys.stdin = open("./3회차/신윤식/_파리퇴치.txt")

T = int(input())

for _ in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [list(map(int,input().split())) for i in range(N)]
    lst = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for a in range(i, i+M):
                for b in range(j, j+M):
                    sum += matrix[a][b]
            lst.append(sum)
    lst.sort()
    print(f'#{_} {lst[-1]}')