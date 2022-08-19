import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)] # 흰칸 = 1 검은 칸 = 0 
    result_a = 0                        # 가로에서 단어를 놓을 수 있는 결과를 저장해주는 변수
    result_b = 0                        # 세로에서 ...
    for i in range(N):
        cnt_a = 0                       # 가로에서 흰 칸의 수를 세어줄 변수
        cnt_b = 0                       # 세로에서 ...
        for j in range(N):                    
            
            if board[i][j] == 1:        # 흰 칸을 만나면
                cnt_a += 1              # cnt_a = + 1
            
            if board[i][j] == 0 or j == N-1:    # 검은 칸을 만나거나 j가 마지막 위치라면
                if cnt_a == K:                  # cnt_a가 K와(단어 글자 수) 같은지 확인
                    result_a +=1                # 결과를 + 1 해준다
                cnt_a = 0                       # 위 조건 문에 들어왔다면 cnt_a를 0으로 초기화

# ==========================================
            if board[j][i] == 1:            # 가로와 같음. i와 j의 위치를 바꿔줌으로써 어떻게 탐색할지만 바꿔준다.
                cnt_b += 1
            
            if board[j][i] == 0 or j == N-1:
                if cnt_b == K:
                    result_b +=1
                cnt_b = 0

    # 출력문

    print(f'#{tc} {result_a + result_b}')   




# 접근했다가 실패한 방식


#             if j < N-2:
#                 if cnt_a == K and board[i][j+1] == 0:              # 3이면 결과를 1 더해준다.. 이상 넘어가면 포함하지 않는다는 것을 어떻게 작성할까..
#                     result_a += 1 
            
#             if j == N-2:
#                 if cnt_a == K-1 and board[i][j+1] == 1:
#                     result_a += 1
# # ==========================================
#             if board[j][i] == 1:
#                 cnt_b += 1
#             else:
#                 cnt_b = 0
            
#             if j < N-2:
#                 if cnt_b == K and board[j+1][i] == 0:              # 3이면 결과를 1 더해준다.. 이상 넘어가면 포함하지 않는다는 것을 어떻게 작성할까..
#                     result_b += 1 
            
#             if j == N-2:
#                 if cnt_b == K-1 and board[j+1][i] == 1:
#                     result_b += 1 

#       한 행과 열에 result 값이 하나만 들어갈 수 있는 줄 알았다.. 정신차리고 문제를 잘 보자