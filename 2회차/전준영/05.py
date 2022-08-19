import sys
input=sys.stdin.readline
answer=[]
metrix=[]
an=[]
ls=[]
T=int(input())
for __ in range(T):
    temp=[]
    ls.clear()
    metrix.clear()
    an.clear()
    ls=list(map(int,input().split()))
    an=[0]*ls[0]
    metrix=list(map(int,input().split()))
    for i in metrix:
        an[i-1]=1
    cnt=1
    for k in an:
        if(k==0):
            temp.append(cnt)
        cnt+=1
    answer.append(temp)
cnt=1
for i in answer:
    print('#'+str(cnt),end=' ')
    cnt+=1
    for k in i:
        print(k,end=' ')
    print()


