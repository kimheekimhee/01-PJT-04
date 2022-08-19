t = int(input())
for _ in range(1,t+1):
    n, m = map(int,input().split())
    fly = [list(map(int,input().split())) for i in range(n)]
    flynum=[]
    icnt = 0
    jcnt = 0
    flysum = 0
    for k in range((n-m+1)**2):
        for i in range(icnt,m+icnt):
            for j in range(jcnt,m+jcnt):
                flysum+=fly[i][j]
        flynum.append(flysum)
        flysum=0
        jcnt+=1
        if m+jcnt>n:
            jcnt = 0
            icnt+=1
        if m+icnt>n:
            break
    result = max(flynum)
    print(f'#{_}',result)
