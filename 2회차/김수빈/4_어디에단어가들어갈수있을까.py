import sys
sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for _ in range(1, T + 1):
    N, K = map(int, input().spilt())
    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input())))

        print(f'#{T}')
