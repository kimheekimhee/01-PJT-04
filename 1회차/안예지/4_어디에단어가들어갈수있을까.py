import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
"""
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
"""
# matrix = [['0', '0', '1', '1', '1'],
#         ['1', '1', '1', '1', '0'],
#         ['0', '0', '1', '0', '0'],
#         ['0', '1', '1', '1', '1'],
#         ['1', '1', '1', '0', '1']]
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = []
    for r in range(N):
        matrix.append(input().split())
    from pprint import pprint
    # pprint(matrix)
    cnt = 0
    word = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == '0':
                if cnt == K:
                    word += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            word += 1
        cnt = 0  
    # transed_matrix = [['0', '1', '0', '0', '1'],
    #                 ['0', '1', '0', '1', '1'],
    #                 ['1', '1', '1', '1', '1'],
    #                 ['1', '1', '0', '1', '0'],
    #                 ['1', '0', '0', '1', '1']] 
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
    
    
    