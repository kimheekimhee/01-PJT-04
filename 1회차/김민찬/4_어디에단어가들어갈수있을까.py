import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())
for _ in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))
    # 배열 받기
    result = 0
    count = 0

    for j in range(N): # j = 행, k = 열
        for k in range(N):
            if puzzle[j][k] == 1:
                count += 1
            if puzzle[j][k] == 0 or k == N - 1: # 0을 만났거나 벽을 만났을 때
                if count == K: # 이전에 계산한 카운트가 K 라면 result에 카운트
                    result += 1
                count = 0 # 카운트 초기화

    for k in range(N): # j = 행, k = 열
        for j in range(N):
            if puzzle[j][k] == 1: # 1이면 카운트
                count += 1
            if puzzle[j][k] == 0 or j == N - 1 :  # 0을 만났거나 벽을 만났을 때
                if count == K:   # 이전에 계산한 카운트가 k 라면 result에 카운트
                    result += 1
                count = 0

    print(f'#{_}', result)