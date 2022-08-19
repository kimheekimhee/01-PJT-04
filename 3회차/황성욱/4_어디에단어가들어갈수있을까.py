
import sys
from pprint import pprint
sys.stdin = open("_어디에단어가들어갈수있을까.txt")
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    # 행 순회
    for row in range(n):
        cnt = 0
        for col in range(n):
            if matrix[row][col] == 1: # 행렬의 요소가 1이면 cnt에 0을 더해줌
                cnt += 1
            
            if matrix[row][col] == 0 or col == n - 1: # 행렬의 요소가 0이거나, 행의 마지막 요소를 조회할 때,
                if cnt == k: # cnt 가 k면 res에 1을 더해줌
                    res += 1
                cnt = 0
    
    # 열 순회 > 행과 동일
    for row in range(n):
        cnt = 0 
        for col in range(n):
            if matrix[col][row] == 1:
                cnt += 1
            
            if matrix[col][row] == 0 or col == n - 1:
                if cnt == k:
                    res += 1
                cnt = 0
            # print(f'배열 {col} {row} {matrix[col][row]} 카운트 {cnt} 결과 {res}')
            
            
    print(f'#{i + 1} {res}')
