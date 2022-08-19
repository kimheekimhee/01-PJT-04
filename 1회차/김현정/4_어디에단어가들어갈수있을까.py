# 정답을 맞추지 못한 문제입니다.
# 결과는 출력이 되나 정답이 아닙니다.

import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

# 테스트케이스 수 변수 선언
T = int(input())

# T 갯수만큼의 테스트케이스 처리
for h in range (1, T+1):
    # 퍼즐 담는 배열 N, 단어 자리수 K 입력받음
    N, K = map(int, input().split())

    # 퍼즐 담는 배열 N_list 정의
    N_list = [list(map(int, input().split())) for _ in range(N)]

    N_row_sum = 0
    N_column_sum = 0

    # 가로
    for i in range(N):
        N_sum = 0
        cnt = 0
        for j in range(N):
            if N_list[i][j] == 1:
                cnt += 1

                if cnt == K:
                    if j < N-1:
                        if N_list[i][j+1] == 1:
                            j = j+1
                            break
            else:
                cnt -= 0
        
            if cnt == K:
                N_sum += 1
                break
        N_row_sum += N_sum

    # 세로
    for i in range(N):
        N_sum = 0
        cnt = 0
        for j in range(N):
            if N_list[j][i] == 1:
                cnt += 1

                if cnt == K:
                    if j < N-1:
                        if N_list[i][j+1] == 1:
                            j = j+1
                            break
            else:
                cnt -= 0
        
            if cnt == K:
                N_sum += 1
                break
        N_column_sum += N_sum

    print(f"#{h}", N_row_sum+N_column_sum)
    print(N_row_sum, N_column_sum)