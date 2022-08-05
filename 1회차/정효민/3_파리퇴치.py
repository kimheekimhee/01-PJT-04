from pprint import pprint
import sys


sys.stdin = open("_파리퇴치.txt")
T = int(input())
for test_case in range(1, T + 1):
    a = 0
    main_mat = []
    n , m = map(int , input().split())
    for _ in range(n):
        line = list(map(int, input().split()))
        main_mat.append(line)
    for x in range(m):
        for y in range(m):
        
            print(main_mat[x][y] ,end ='')
              
                
