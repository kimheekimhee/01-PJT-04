import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

n = int(input())
grid = []
a, b = map(int, input().split())
cnt = 0
garo = 0
for _ in range(1, n + 1):
    for i in range(a):
        line = list(input())
        grid.append(line)
    for i in range(a):
        for j in range(a):
            if grid[i][j] == '0':
                cnt = 0
            else:
                cnt += 1
                if cnt == b:
                    garo += 1
        cnt = 0

print(cnt)

    
    
