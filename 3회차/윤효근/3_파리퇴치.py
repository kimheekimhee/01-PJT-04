import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
result=[]
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    board = [[] * n for _ in range(n)]
    for i in range(n):
        box = list(map(int,input().split()))
        for j in range(n):
            board[i].append(box[j])
    for i in range(n-m+1):
        for j in range(n-m+1):
            max_kill=0
            for x in range(m):
                for y in range(m):
                    max_kill += board[i+x][j+y]
                result.append(max_kill)

    print(f'#{test_case} {max(result)}')
    result=[]
