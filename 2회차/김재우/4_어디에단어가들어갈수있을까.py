import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result_a = 0 
    result_b = 0 
    for i in range(N):
        cnt_a = 0  
        cnt_b = 0
        for j in range(N):                    
            if board[i][j] == 1:
                cnt_a += 1
            else:
                cnt_a = 0
            
            if j < N-2:
                if cnt_a == K and board[i][j+1] == 0:              # 3이면 결과를 1 더해준다.. 이상 넘어가면 포함하지 않는다는 것을 어떻게 작성할까..
                    result_a += 1 

                elif cnt_a == K-1 and board[i][j+1] == 1:
                    result_a += 1
             
# ==========================================
            if board[j][i] == 1:
                cnt_b += 1
            else:
                cnt_b = 0
            
            if j < N-2:
                if cnt_b == K and board[j+1][i] == 0:              # 3이면 결과를 1 더해준다.. 이상 넘어가면 포함하지 않는다는 것을 어떻게 작성할까..
                    result_b += 1 

                elif cnt_b == K-1 and board[j+1][i] == 1:
                    result_b += 1

    print(f'#{tc} {result_a + result_b}')

        

           # if j <= N-2:                        # j가 N[3] 보다 작거나 같을 때
            #     if j == N-2:                    # j가 N[3] 이면
            #         if cnt_a == (K-1):          # cnt가 2일 경우
            #             if board[i][j+1] == 1:  # N[4]가 1인지 확인하고
            #                 result_a += 1       # result 증가
            #     if cnt_a == K:                  # cnt 가 3일경우
            #         if board[i][j+1] == 0:      # 다음 N 위치가 0이라면
            #             result_a += 1           # result 증가



                        # if j <= N-2:                        # j가 N[3] 보다 작거나 같을 때
            #     if j == N-2:                    # j가 N[3] 이면
            #         if cnt_a == (K-1):          # # cnt가 2일 경우
            #             if board[j+1][i] == 1:  # N[4]가 1이라면
            #                 result_a += 1       # result 증가
            #     if cnt_b == K:                  # cnt 가 3일 경우 
            #         if board[j+1][i] == 0:      # 다음 N이 0이라면
            #             result_b += 1           #  result 증가