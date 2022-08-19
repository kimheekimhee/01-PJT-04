import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())                                # 테스트케이스 개수

for test_case in range(1, T+1):
    N, K = map(int, input().split())            # 퍼즐 크기, 단어 길이

    puzzle = []                                 # 퍼즐 상황
    for i in range(N):                          # 2차원 배열
        puzzle.append(list(map(int, input().split())))
    
    garo = 0                                    # 가로 들어갈 수 있는 자리 수
    for i in range(N):                          # 가로 확인
        cnt = 0                                 # 흰색 길이
        for j in range(N):
            if puzzle[i][j] == 1:               # 흰색 자리이면
                cnt += 1                        # 흰색 길이 +1
            if puzzle[i][j] == 0 or j == N-1:   # 검은 자리나 퍼즐 끝일 때
                if cnt == K:                    # 지금까지 흰색 길이가 단어 길이와 같으면
                    garo += 1                   # 단어 넣을 수 있음
                if puzzle[i][j] == 0:           # 검은 자리이면
                    cnt = 0                     # 흰색 길이 초기화

    sero = 0                                    # 세로 들어갈 수 있는 자리 수
    for j in range(N):                          # 세로 확인
        cnt = 0                                 # 흰색 길이
        for i in range(N):
            if puzzle[i][j] == 1:               # 흰색 자리이면
                cnt += 1                        # 흰색 길이 +1
            if puzzle[i][j] == 0 or i == N-1:   # 검은 자리나 퍼즐 끝일 때
                if cnt == K:                    # 지금까지 흰색 길이가 단어 길이와 같으면
                    sero += 1                   # 단어 넣을 수 있음
                if puzzle[i][j] == 0:           # 검은 자리이면
                    cnt = 0                     # 흰색 길이 초기화

    print(f'#{test_case} {garo + sero}')        # 들어갈 수 있는 자리 수 출력