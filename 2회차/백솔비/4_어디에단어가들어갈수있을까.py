import sys
sys.stdin = open("_어디에단어가들어갈수있을까.txt")
# 어제 풀었던 누울 자리를 찾아라 같은 문제

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 이차원 배열로 받아줍니다.
    board = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    cnt = 0

    # 행 먼저 탐색하면서 1이 나오면 카운트 해주고 K의 값과 같으면 total에 하나씩 더해줍니다.
    # 한 줄씩 탐색하므로 줄이 넘어갈 때마다 cnt를 0으로 초기화해줍니다.
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                if cnt == K:
                    total += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            total += 1
        cnt = 0
    
    # 열 탐색도 행 탐색과 똑같이 수행합니다.
    for i in range(N):
        for j in range(N):
            if board[j][i] == 0:
                if cnt == K:
                    total += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            total += 1
        cnt = 0

    print(f'#{tc} {total}')