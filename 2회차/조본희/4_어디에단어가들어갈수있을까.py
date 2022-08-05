import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

def puzzlesolver(puzzle, N, K):
    ans = 0
    for i in range(N):
        temp = 0
        for j in range(N):
            if puzzle[i][j] == 0:
                if temp == K:
                    ans += 1
                temp = 0
            elif puzzle[i][j] == 1:
                temp += 1
        if temp == K:
            ans += 1
    return ans

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    puzzle2 = list(map(list, zip(*puzzle)))
    
    ans = puzzlesolver(puzzle, N, K) + puzzlesolver(puzzle2, N, K)
    print(f'#{test_case} {ans}')