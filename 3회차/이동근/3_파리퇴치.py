T = int(input())

for i in range(T):
    N, M = map(int, input().split())

    dx = [j for j in range(M)]
    dy = [j for j in range(M)]
    
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # DP 문제 같은데 DP 를 사용할 줄 모르겠다.
    # 브루트 포스를 사용했다.
    count = 0
    for j in range(N - M + 1):
        for k in range(N - M + 1):
            now = 0

            for l in range(M):
                for m in range(M):
                    now += grid[j + dy[l]][k + dx[m]]

            if count < now:
                count = now
            
    print(f"#{i + 1}", count)