import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

from pprint import pprint

T = int(input())

for t in range(1, T+1):
    n, k = list(map(int, input().split()))

    matrix = [list(map(int, input().split())) for _ in range(n)]

    sum_cnt = 0
    for row in range(n):
        cnt = 0
        for col in range(n):
            if matrix[row][col] == 0:
                if cnt == k:
                    sum_cnt += 1
                cnt = 0
            else:
                cnt += 1

        if cnt == k:
            sum_cnt += 1
            
    for col in range(n):
        cnt = 0
        for row in range(n):
            if matrix[row][col] == 0:
                if cnt == k:
                    sum_cnt += 1
                cnt = 0
            else:
                cnt += 1
                
        if cnt == k:
            sum_cnt += 1


    print(f'#{t} {sum_cnt}')