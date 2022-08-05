import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(a)]
    result = []
    for i in range(a-b+1):
        for j in range(a-b+1):
            bug = 0
            for x in range(b):
                for y in range(b):
                    bug += matrix[i+x][j+y]
            result.append(bug)
    print(f'#{i}', max(result))