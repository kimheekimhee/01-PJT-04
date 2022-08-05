# D2-어디에 단어가 들어갈 수 있을까



# 입력
'''
1. 테스트 케이스 수 T
2. 단어 퍼즐의 가로세로 길이 N, 단어의 길이 K
- 5 <= N <= 15
- 2 <= K <= N
3. N개의 줄에 퍼즐 정보
- 1: 흰색 칸
- 0: 검정 칸
'''



# 출력
'''
1. #{해당 테스트케이스} + {길이가 K인 단어가 퍼즐 내 들어갈 수 있는 곳 갯수}
'''


# 코드 1
import sys

sys.stdin = open("input_text/_어디에단어가들어갈수있을까.txt")

# 각 행을 둘러보면서 길이가 K인 단어가 들어갈 수 있는 곳 카운트
def cnt_K(matrix, K):
    cnt_K = 0
    for row in matrix:
        cnt = 0
        for block in row:
            if block == '0':
                if cnt == K:
                    cnt_K += 1
                cnt = 0   # 초기화
            else:
                cnt += 1

        if cnt == K:
            cnt_K += 1
        
    return cnt_K


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    tot_cnt = 0

    # 가로줄 중 길이가 K인 단어가 들어갈 수 있는 곳 카운트
    puzzle = [input().split() for _ in range(N)]
    tot_cnt += cnt_K(puzzle, K)

    # 행렬이 바뀐 퍼즐 만들기
    new_puzzle = [[None] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_puzzle[c][r] = puzzle[r][c]

    # 세로줄 중 길이가 K인 단어가 들어갈 수 있는 곳 카운트
    tot_cnt += cnt_K(new_puzzle, K)

    print(f'#{test_case} {tot_cnt}')



# 실행시간(메모리:56,936 kb, 시간:134 ms)



# 코드 2
import sys

sys.stdin = open("input_text/_어디에단어가들어갈수있을까.txt")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    tot_cnt = 0

    # 가로줄 중 길이가 K인 단어가 들어갈 수 있는 곳 카운트
    puzzle = [input().replace(' ', '') for _ in range(N)]
    for row in puzzle:
        for section in row.split('0'):
            if len(section) == K:
                tot_cnt += 1

    # 행렬이 바뀐 퍼즐 만들기
    new_puzzle = [''.join(row) for row in zip(*puzzle)]

    # 세로줄 중 길이가 K인 단어가 들어갈 수 있는 곳 카운트
    for row in new_puzzle:
        for section in row.split('0'):
            if len(section) == K:
                tot_cnt += 1

    print(f'#{test_case} {tot_cnt}')



# 실행시간(메모리:56,944 kb, 시간:134 ms)