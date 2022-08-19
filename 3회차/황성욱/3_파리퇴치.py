import sys

sys.stdin = open("_파리퇴치.txt")
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    score = []
    for j in range(n - m + 1):
        for k in range(n - m + 1): # 행렬을 순회할 때, n - m + 1 (5 - 2 + 1)
            sum_val = 0 # 행렬의 요소에서 m * m 만큼 요소의 값을 더해줌
            for q in range(m):
                for p in range(m):
                    ny = j + q # 정사각형의 배열이라 순서는 크게 상관이 없는 것 같음
                    nx = k + p
                    sum_val += matrix[ny][nx]
            score.append(sum_val)
    print(f'#{i + 1} {max(score)}')