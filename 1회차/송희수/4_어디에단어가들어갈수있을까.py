from re import L
import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for tc in range(1,T+1):
    N, K = map(int, input().split(' '))
    matrix = [list(map(int, input().split())) for a in range(N)]
    cnt = 0
    result = 0
    for i in range(N):
        for j in range(N):
            # 요소가 1일때 1더한다. #행을 기준으로 구한다.
            if matrix[i][j] == 1:
                cnt += 1
            # 요소가 0을 만나거나 벽을 만났을때
            if matrix[i][j] == 0 or j == N-1:
                if cnt == K:
                    result += 1 # 1110111인 경우 각각을 더한다.
                cnt = 0 #이런경우 0으로 초기화한다.
        for j in range(N):
            if matrix[j][i] == 1:
                cnt += 1
            if matrix[j][i] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                cnt = 0

    print(f'#{tc} {result}')
    
