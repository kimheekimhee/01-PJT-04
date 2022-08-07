import sys
sys.stdin = open("_파리퇴치.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = []
    
    for _ in range(N):
        board.append([*map(int, input().split())])
    
    dead_flies = []
    
    for i in range(N - (M - 1)):
        for j in range(N - (M - 1)):
            total = 0
            for x in range(i, i + M):
                for y in range(j, j + M):
                    total += board[x][y]
            
            dead_flies.append(total)
    
    print(f"#{test_case} {max(dead_flies)}")

# for 문 저렇게 쓰는거 맞나? 백준이었으면 통과 못했을 것 같다.