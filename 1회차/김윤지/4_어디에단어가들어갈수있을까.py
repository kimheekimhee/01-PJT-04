import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

t = int(input())

for tc in range(1,t+1):
    n, k = map(int,input().split())
    puzzle = [list(map(int,input().split()))for _ in range(n)]
    cnt = 0    
    total = 0

    for i in range(n):
        for j in range(n):#가로
            if puzzle[i][j] == 1: #위치에 1이 있으면 1더하기
                cnt +=1
            if puzzle[i][j]== 0 or j == n-1: #0또는 마지막열일때
                if cnt == k: #카운트가 k와 같다면
                    total += 1 #토탈에 1더하기
                cnt = 0    #카운트 초기화

        for j in range(n): #세로
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == n-1:#0또는 마지막행일때
                if cnt == k:
                    total += 1
                cnt = 0

    
    print(f'#{tc} {total}')                
