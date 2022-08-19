from pprint import pprint
import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())   
    arr = []

    for _ in range(N):
        n = input().split()
        arr.append(n)
    
    cnt = 0
    score = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                cnt += 1
                if cnt == 3:
                    score += 1
                    cnt = 0
            else:
                cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[j][i] != 0:
                cnt += 1
                if cnt == 3:
                    score += 1
                    cnt = 0
            else:
                cnt = 0
    
    print(type(arr))
    print(score)