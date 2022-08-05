import sys

sys.stdin = open("_파리퇴치.txt")

input = sys.stdin.readline
T = int(input())

for i in range(T): # 테스트 갯수
    N, M = map(int,input().split()) # NxN행렬, 파리채크기
    matrix = [list(map(int,input().split())) for _ in range(N)] # 배열 받기
    SUM = [] # 모든 경우 기록
    for j in range(N-(M-1)): # 구간 !
        for k in range(N-(M-1)):
            sum = 0
            for ii in range(M):
                for jj in range(M):
                    sum += matrix[j+ii][k+jj]
            SUM.append(sum)
    print(f'#{i+1} {max(SUM)}')