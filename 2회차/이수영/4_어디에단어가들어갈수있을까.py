import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
T = int(input())

N, M = map(int, input().split())
matrix = [list(input().split()) for _ in range(N)]
print(matrix)
a, b = 0, 0
lenth_a = 0
lenth_b = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '1':
            lenth_a += 1
        else:
            lenth_a == 0
        if lenth_a == 3:
            a += 1

        if matrix[j][i] == '1':
            lenth_b += 1
        else:
            lenth_b == 0
        if lenth_b == 3:
            b += 1
print(a, b)