import sys

sys.stdin = open("_파리퇴치.txt")
input = sys.stdin.readline
T = int(input())

for test_case in range(1, T+1):
    catch_lst = []
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dx = list(range(M))*M
    dy = [i for i in range(M) for _ in range(M)]
    for i in range(N):
        for j in range(N):

            catch = 0
            for k in range(M*M):
                y = i+dy[k]
                x = j+dx[k]
                if 0 <= x <= N-1 and 0 <= y <= N-1:
                    catch += matrix[y][x]
            catch_lst.append(catch)
    print(f'#{test_case} {max(catch_lst)}')
            