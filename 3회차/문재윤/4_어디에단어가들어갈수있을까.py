import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")


n = int(input())
for iii in range(1,1+n):
    a, b = map(int,input().split())
    puzzl = [list(map(int, input().split())) for _ in range(a)]
    answer = 0
    
    for i in range(a):
        cou = 0
        for j in range(a):
            if puzzl[i][j] == 1:
                cou += 1
            if puzzl[i][j] == 0 or j == a-1:
                if cou == b:
                    answer += 1
                cou = 0


    for k in range(a):
        coun = 0
        for h in range(a):
            if puzzl[h][k] == 1:
                coun += 1
            if puzzl[h][k] == 0 or h == a-1:
                if coun == b:
                    answer += 1
                coun = 0


    print(f'#{iii} {answer}')