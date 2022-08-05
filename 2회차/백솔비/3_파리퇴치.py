import sys
sys.stdin = open("_파리퇴치.txt")

T = int(input())
result = []

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 이차원 리스트로 파리 목록을 구성해줍니다.
    fly = [list(map(int, input().split())) for _ in range(N)]

    kill = 0
    # 전체 파리 크기에서 파리채가 그 범위를 벗어나면 안되므로 N-M+1로 범위를 설정합니다.
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            tmp = 0
            # 파리채의 범위를 구성합니다.
            for x in range(M):
                for y in range(M):
                    # 파리채가 떄린 범위 안의 수를 더합니다.
                    tmp += fly[i+x][j+y]
            # 가장 많은 파리가 죽은 자리를 찾습니다.
            if tmp > kill:
                kill = tmp
    result.append(kill)

for a in range(T):
    print(f'#{a + 1} {result[a]}')

