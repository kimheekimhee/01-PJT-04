import sys

sys.stdin = open("_파리퇴치.txt")

tc=int(input())
for t in range(tc):
    n,m=map(int, input().split())
    enemies=[list(map(int, input().split())) for _ in range(n)]
    result=[]
    for i in range(n-m+1): # 파리가 있는 배열 탐색
        for j in range(n-m+1):
            tmp=0
            for x in range(m): # 파리채의 크기 m 만큼 탐색
                for y in range(m):
                    try :tmp+=enemies[x+i][y+j]
                    except : continue
            result.append(tmp)
    print(f'#{t+1}',max(result))
    

            

