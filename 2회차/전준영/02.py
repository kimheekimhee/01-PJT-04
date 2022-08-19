import sys
input=sys.stdin.readline
answer=[0]*10
metrix=[]
input()
column=[]
cnt=0
for _ in range(10):
    ls=list(map(int,input().split()))
    N=ls[0]
    M=ls[1]
    metrix.clear()
    column.clear()
    column=[0]*N
    for i in range(N):
        metrix.append(list(map(int,input().split())))
    for k in metrix:
        row0=0
        column0=0
        for j in k:
            if(j==1):
                column[column0]+=1
                row0+=1
            else:
                if column[column0]==M:
                    answer[cnt]+=1
                if row0==M:
                    answer[cnt]+=1
                row0=0
                column[column0]=0
            column0+=1
        if(row0==M):
            answer[cnt]+=1
    for m in column:
        if(m==M):
            answer[cnt]+=1
    cnt+=1
cnt=1    
for j in answer:
    print('#'+str(cnt),j)
    cnt+=1