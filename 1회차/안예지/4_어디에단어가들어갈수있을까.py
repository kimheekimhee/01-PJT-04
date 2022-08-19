# Solving Club 2주차 모의고사

"""
N X N 크기의 단어 퍼즐의 모양이 주어진다.

특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램 작성하기

# 입력
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.

10
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1

# 출력
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력

# 접근 방법
1. 단어 퍼즐을 순회하면서 벽 혹은 퍼즐의 끝을 만났을 때 
2. 세어 온 빈 공간의 크기가 특정 길이 K를 만족하면
3. 필요한 자리의 수를 더한다.

"""
import sys
sys.stdin = open("_어디에단어가들어갈수있을까.txt")
from pprint import pprint

# 1

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())

    # 단어 퍼즐 받아올 반복문
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # pprint(matrix)
    box = 0
    slot = 1
    # 자리의 수를 저장할 변수
    word_cnt = 0
    # 빈 공간 수를 저장할 변수
    white = 0
    for r in range(N):
        for c in range(N):
            # 현재 칸이 빈 공간이라면 빈 공간 수+= 1
            if matrix[r][c] == slot:
                white += 1
            
            # 현재 칸이 박스 칸이라면
            # 빈 공간 수 초기화
            if matrix[r][c] == box:
            # 빈 공간 수가 K의 길이와 같아지면 자리의 수 += 1
            # 하고 세어온 빈 공간 수 초기화    
                if white == K:
                    word_cnt += 1
                white = 0
            
        # 한 행 탐색이 끝났는데 빈 공간의 수가 K라면,
        # 자릿수 += 1
        # 행의 탐색이 끝났으므로 빈 공간 수 초기화
        if white == K:
            word_cnt += 1
        white = 0

    # print(word_cnt)

    # 상하 열 우선 탐색을 위한 반복문
    for c in range(N):
        for r in range(N):
            if matrix[r][c] == slot:
                white += 1
                
            if matrix[r][c] == box:
                if white == K:
                    word_cnt += 1
                white = 0
            
        if white == K:
            word_cnt += 1
        white = 0
        
    # print(word_cnt)
    print(f'#{t} {word_cnt}')




# 2
"""
# matrix = [['0', '0', '1', '1', '1'],
#         ['1', '1', '1', '1', '0'],
#         ['0', '0', '1', '0', '0'],
#         ['0', '1', '1', '1', '1'],
#         ['1', '1', '1', '0', '1']]
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    # 주어진 리스트를 받아오기 위한 반복문
    matrix = []
    for r in range(N):
        matrix.append(input().split())
   
    # pprint(matrix)
    # 빈 공간의 수를 저장할 변수
    cnt = 0
    # 자리의 수를 저장할 변수
    word = 0
    # 이차원 리스트 순회를 위한 이중반복문
    for r in range(N):
        for c in range(N):
            # 현재 위치가 벽이고,
            # 빈 공간의 수가 K 개라면,
            # += 자리의 수
            # 자리 수가 추가되면 빈 공간 수는 초기화
            if matrix[r][c] == '0':
                if cnt == K:
                    word += 1
                cnt = 0
            # 현재 위치가 빈 공간이라면
            # += 빈 공간의 수
            else:
                cnt += 1
                
        # 하나의 행을 탐색하고 나서
        # 빈 공간의 수가 K개라면, 단어가 들어갈 수있는 자리의 수 + 1
        if cnt == K:
            word += 1
        # 지금껏 세온 빈 공간의 수는 초기화
        cnt = 0  
    # transed_matrix = [['0', '1', '0', '0', '1'],
    #                 ['0', '1', '0', '1', '1'],
    #                 ['1', '1', '1', '1', '1'],
    #                 ['1', '1', '0', '1', '0'],
    #                 ['1', '0', '0', '1', '1']] 
    
    # 좌우 행우선 순회를 위해 행렬 전치
    transed_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for c in range(len(matrix[0])):
        for r in range(len(matrix)):
            transed_matrix[c][r] = matrix[r][c]
    # pprint(transed_matrix)

    for r in range(len(transed_matrix)):
        for c in range(len(transed_matrix[0])):
            if transed_matrix[r][c] == '0':
                if cnt == K:
                    word += 1
                cnt = 0
        
            else:
                cnt += 1
        if cnt == K:
            word += 1
        cnt = 0
    print(f'#{t} {word}')

"""
    
    