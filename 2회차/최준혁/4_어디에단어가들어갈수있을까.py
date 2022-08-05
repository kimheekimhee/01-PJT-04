# import sys

# sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for _ in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for __ in range(N)]
    result = 0
    for c in range(N):
        cnt = 0
        cnt2 = 0
        for r in range(N):
            # 열 검사 
            if puzzle[c][r] == 1:
                cnt += 1
            if puzzle[c][r] == 0 or r == N-1: # 검은벽(0)을 만나거나 r의 값이 N-1길이와 같다면  
                if cnt == K: # 카운트가 입력한 K값과 같으면
                    result += 1 # 결과값 1 증가
                cnt = 0
            # 행 검사 
            if puzzle[r][c] == 1: # 흰색(1)이면 
                cnt2 += 1 # 카운트 증가
            if puzzle[r][c] == 0 or r == N-1: # 검은벽(0)을 만나거나 r의 값이 N-1길이와 같다면  
                if cnt2 == K: # 카운트가 입력한 K값과 같다면 
                    result += 1 # 결과값 1증가
                cnt2 = 0 # 그외에 0으로 초기화

    print("#{} {}".format(_, result))
