import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    fly =[list(map(int, input().split())) for _ in  range(N)]
    
    all_total = []
    for a in range(N-M+1):
        for b in range(N-M+1):
            total = []
            for c in range(M):
                total.append(fly[a+c][b:b+M])
            
            all_total.append(sum(map(sum, total)))
    
    print(f'#{test_case} {max(all_total)}')

    