import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

tc=int(input())
for t in range(tc):
    n,word = map(int, input().split())
    crossboard = [list(map(int, input().split())) for _ in range(n)]
    tr_crossboard = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tr_crossboard[i][j] = crossboard[j][i]
    result=0
    for i in crossboard:
        cnt=0
        for j in i:
            if j == 1 :
                cnt += 1
            if j == 0 :
                if cnt == word :
                    result += 1
                cnt = 0
        if cnt == word :
            result += 1
    for i in tr_crossboard:
        cnt=0
        for j in i:
            if j == 1 :
                cnt += 1
            if j == 0 :
                if cnt == word :
                    result += 1
                cnt = 0
        if cnt == word :
            result += 1
    print(f'#{t+1}',result)
