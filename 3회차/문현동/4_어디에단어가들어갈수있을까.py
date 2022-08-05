import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for test_case in range(1, T + 1):
    
    N, K = map(int, input().split())
    
    puzzle = []
    row_p = 0
    column_p = 0
    
    for _ in range(N):
        puzzle.append([*map(int, input().split())])
        
    for row in puzzle:
        space = 0
        for cell in row:
            if cell == 1:
                space += 1
            else:
                if space == K:
                    row_p += 1
                    space = 0
                else:
                    space = 0
                    continue
        if space == K:
            row_p += 1
            
    for row in range(len(puzzle)):
        space = 0
        for column in range(len(puzzle[row])):
            if puzzle[column][row] == 1:
                space += 1
            else:
                if space == K:
                    column_p += 1
                    space = 0
                else:
                    space = 0
                    continue
        if space == K:
            column_p += 1
            
    print(f"#{test_case} {row_p + column_p}")