import sys

sys.stdin = open("_파리퇴치.txt")
T = int(input())


for tc in range(1, T + 1):
   
    N, M = map(int, input().split())


    mat = [list(map(int, input().split())) for _ in range(N)]

   
    fly = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for ci in range(M):
                for cj in range(M):
                    if i + ci in range(N) and j + cj in range(N):
                        total += mat[i + ci][j + cj]           
            fly.append(total)
    

    max_value = fly[0]
    for i in fly:
        if i > max_value:
            max_value = i

    print('#{} {}'.format(tc, max_value))