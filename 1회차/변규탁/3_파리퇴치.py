import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    fly = [list(map(int, input().split())) for _ in range(N)]

    max_ = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_ = 0
            for r in range(M):
                for c in range(M):
                    sum_ += fly[i+r][j+c]
            max_.append(sum_)
    
    print(f'#{test_case} {max(max_)}')    