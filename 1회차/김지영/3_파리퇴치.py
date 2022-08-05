import sys
from pprint import pprint
sys.stdin = open("_파리퇴치.txt")
T = int(input())
# n*n 배열에서
# m*m 파리채로 가장 큰 수..
# [y,x], [y+1,x],[y,x+1],[y+1,x+1]
# 배열의 범위를 벗어나지 않도록..y+1,x+1 < n
# test_case = T
# n,m = 6,3
# grid = [[29, 21, 26, 9, 5, 8], 
#         [21, 19, 8, 0, 21, 19], 
#         [9, 24, 2, 11, 4, 24], 
#         [19, 29, 1, 0, 21, 19],
#         [10, 29, 6, 18, 4, 3], 
#         [29, 11, 15, 3, 3, 29]]

for test_case in range(1,T+1):

    n,m = map(int,input().split())
    grid = []
    for _ in range(n):
        temp = list(map(int,input().split()))
        grid.append(temp)

    flapper = [] 
    for y in range(0,n):
        for x in range(0,n):
            temp_lst = []
            for i in range(m):
                fly_y = y+i
                for i in range(m):
                    fly_x = x+i
                    if 0<= fly_y <= n-1 and 0<= fly_x<= n-1:
                        temp_lst.append(grid[fly_y][fly_x])
            flapper.append(sum(temp_lst))
    result = max(flapper)
    # print(result)
    print(f'#{test_case}',result)