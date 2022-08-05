import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for i in range(1, T+1):
    matrix = []
    N, M = map(int, input().split())
    
    for j in range(N):
        matrix.append(list(map(int, input().split())))

    dead_pari = []
    for k in range(N-M+1):
        for l in range(N-M+1):
            pari_row = []
            for n in range(M):
                for m in range(M):
                    pari_row.append(matrix[n+k][m+l])
                dead_pari.append(pari_row)

    print(f'#{i} {max(map(sum, dead_pari))}')