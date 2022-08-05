import sys

sys.stdin = open("_파리퇴치.txt")

tc=int(input())
for t in range(tc):
    n,m=map(int, input().split())
    enemies=[list(map(int, input().split())) for _ in range(n)]
    weapon=[]
    result=[]
    for i in range(n-m+1):
        for j in range(n-m+1):
            tmp=0
            for x in range(m):
                for y in range(m):
                    try :tmp+=enemies[x+i][y+j]
                    except : continue
            result.append(tmp)
    print(f'#{t+1}',max(result))
    

            

