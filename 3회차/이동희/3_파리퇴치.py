T = int(input())

N, M = map(int,input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N): # 0,1,2,3,4
    # 시작점에서 파리채의 끝부분이 전체 가로길이를 넘지 않아야한다.
    while i + M-1  < N-1:
        for j in range(N):
            while j + M < N:
                result += sum(matrix[i][j:j+M])