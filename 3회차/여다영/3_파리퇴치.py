import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for _ in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    nums = []
    times = N - M + 1
    for i in range(times):
        for j in range(times):
            sum = 0
            for temp_1 in range(M):
                for temp_2 in range(M):
                    sum += matrix[i+temp_1][j+temp_2]
            nums.append(sum)

    print(f'#{_}', max(nums))