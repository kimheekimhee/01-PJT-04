T = int(input())

for i in range(T):
    N, K = map(int, input().split())

    grid = [input().replace(' ', '') for _ in range(N)]
    col = [''] * N
    for j in range(N):
        for k in range(N):
            col[j] += grid[k][j]

    count = 0
    for j in range(N):
        row_count = 0
        col_count = 0

        for k in range(N):
            if grid[j][k] == '1':
                row_count += 1
            else:
                if row_count == K:
                    count += 1
                row_count = 0
            if col[j][k] == '1':
                col_count += 1
            else:
                if col_count == K:
                    count += 1
                col_count = 0
        
        if row_count == K:
            count += 1
        if col_count == K:
            count += 1

    print(f"#{i + 1}", count)