import sys

sys.stdin = open("_파리퇴치.txt")

t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())
    fly = []

    for j in range(n):
        fly.append(list(map(int, input().split())))

    # 잡을 수 있는 파리 수를 저장할 2차원 리스트 선언
    # 2차원 리스트의 길이는 파리가 있는 리스트 길이에서 파리채의 길이를 뺀 후 1을 더한 길이다.
    result = [[0] * (n - m + 1) for _ in range(n - m + 1)]

    for j in range(n - m + 1):
        for k in range(n - m + 1):              # 파리채가 이동 가능한 곳까지 반복 수행
            sum_ = 0
            for a in range(m):
                for b in range(m):
                    # 파리채의 길이만큼 행, 열로 이동하며 sum_에 파리수를 누적
                    # ex) if m == 2: sum_ = fly[0][0] + fly[0][1] + fly[1][0] + fly[1][1]
                    sum_ += fly[j + a][k + b]
            result[j][k] = sum_                 # 잡을 수 있는 파리의 수를 2차원 리스트에 저장

    print(f'#{i} {max(map(max, result))}')
