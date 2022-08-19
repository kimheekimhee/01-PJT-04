#from pprint import pprint
import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for test_case in range(1,T+1) : 
    N, M = map(int, input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    #pprint(board)
   
    max_sum = 0
    
    for i in range(N - M + 1) :
        for j in range(N - M + 1) :
            sum_ = 0
            for k in range(M) :
                for l in range(M) :
                    sum_ += board[i+k][j+l]
                    if sum_ > max_sum : 
                        max_sum = sum_
    
    print(f'#{test_case} {max_sum}')