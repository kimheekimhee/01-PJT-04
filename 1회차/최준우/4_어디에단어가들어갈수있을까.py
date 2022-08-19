import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for test_case in range(T):
    N, K = map(int, input().split()) # N: 가로, 세로 길이. K: 단어의 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)] # puzzle 모양 입력
    result = 0
    # 가로 체크
    for i in range(N):
        cnt = 0 
        for j in range(N):
            if puzzle[i][j] == 1: # 해당 위치가 흰칸 1 이면 cnt+1.
                cnt += 1
            else: # 1이 아닐때 K값 과 cnt가 같으면 결과변수에 +1
                if cnt == K:
                    result += 1
                cnt = 0 # 0으로 초기화
        else: # 해당 행 다 돌았을때 한번 더 cnt, K값 같은지
            if cnt == K:
                result += 1
    # 세로 체크
    for j in range(N):
        cnt = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        else:
            if cnt == K:
                result += 1
    #출력
    print(f'#{test_case + 1} {result}')