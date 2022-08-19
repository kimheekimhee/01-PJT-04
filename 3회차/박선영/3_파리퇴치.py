import sys

sys.stdin = open("_파리퇴치.txt")

# 10
# 5 2
# 1 3 3 6 7
# 8 13 9 12 8
# 4 16 11 12 6
# 2 4 1 23 2
# 9 13 4 7 3

# #1 49

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    max_sum = 0
    delta_x = []
    delta_y = []
    for y in range(m):                  # 델타x 와 델타y 리스트를 만든다
        for x in range(m):
            delta_x.append(x)
            delta_y.append(y)
    for y in range(n):
        for x in range(n):
            sum_ = 0
            for k in range(len(delta_x)):
                yy = y + delta_y[k]
                xx = x + delta_x[k]

                if 0 <= yy < n and 0 <= xx < n:     # 범위가 벗어나지 않는 지 체크
                    sum_ += matrix[yy][xx]
            if sum_ > max_sum:                      # 최댓값보다 커지면 최댓값을 바꿔줌
                max_sum = sum_
    print(f'#{test_case} {max_sum}')