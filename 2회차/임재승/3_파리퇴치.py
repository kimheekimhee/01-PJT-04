import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for T_case in range(1, T+1):
    N, M = map(int,input().split())
    li = [list(map(int,input().split())) for _ in range(N)]
    result = 0

    # 범위를 초과하지않게 지정해주고 M의 크기만큼 포인트를 더해준다.
    for i in range(N-M+1):
        for j in range(N-M+1):
            point = 0
            for a in range(i, i+M):
                for b in range(j, j+M):
                    point += li[a][b]
            if point > result:
                result = point

    print(f'#{T_case} {result}')