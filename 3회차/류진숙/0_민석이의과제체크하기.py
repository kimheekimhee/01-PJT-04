import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())


for t in range(1, T+1):
    result = []
    n, k = list(map(int, input().split()))

    arr = list(map(int, input().split()))

    matrix = [0] * n

    for i in range(n):
        for a in arr:
            if i == a-1:
                matrix[i] = a

    for j in range(n):
            if matrix[j] == 0:
                result.append(j+1)

    print(f'#{t}', end = ' ')
    print(*result)






            


    