import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for Test_case in range(1, T+1):
    N, K = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    result = []
    # 행을기준으로 렬을 늘려갈때 
    for i in range(N):
        count = 0
        for j in range(N):
            if li[i][j] == 0 and count != 0:
                result.append(count)
                count = 0
            elif li[i][j] == 1:
                count += 1
                if j == N-1:
                    result.append(count)

    for j in range(N):
        count = 0
        for i in range(N):
            if li[i][j] == 0 and count != 0:
                result.append(count)
                count = 0
            elif li[i][j] == 1:
                count += 1
                if i == N-1:
                    result.append(count)
    print(f'#{Test_case} {result.count(K)}')
    
