import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    wsum = 0
    lsum = 0
    ans = 0
    for i in range(n):
        for j in range(n):
            # 가로 먼저 셈
            if puzzle[i][j] == 1:
                wsum += 1
            elif puzzle[i][j] == 0:
                if wsum == k:
                    ans += 1
                wsum = 0
            if j == n-1:
                if wsum == k:
                    ans += 1
                wsum = 0


            # 세로
            if puzzle[j][i] == 1:
                lsum += 1
            elif puzzle[j][i] == 0:
                if lsum == k:
                    ans += 1
                lsum = 0
            if j == n-1:            # 여기 자꾸 i == n-1로 실수하는데 고치기!!!!!
                if lsum == k:
                    ans += 1
                lsum = 0


    print(f'#{test_case} {ans}')