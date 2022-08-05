import sys
input=sys.stdin.readline
answer=[]
metrix=[]
sum=[]
T=int(input())
for __ in range(T):
    max=0
    input0=list(map(int,input().split()))
    metrix.clear()
    for _ in range(input0[0]):
        metrix.append(list(map(int,input().split())))
    sum=[[0]*input0[0] for ___ in range(input0[0])]
    for i in range(input0[0]):
        for k in range(input0[0]):
            if(k>0):
                sum[i][k]=sum[i][k-1]+metrix[i][k]
            else:
                sum[i][k]=metrix[i][k]
    for i in range(input0[0]-input0[1]+1):
        for k in range(input0[0]-input0[1]+1):
            temp=0
            for j in range(input0[1]):
                temp+=sum[i+j][k+input0[1]-1]-sum[i+j][k]+metrix[i+j][k]
            if(temp>max):
                max=temp
    answer.append(max)
cnt=1
for j in answer:
    print('#'+str(cnt),j)
    cnt+=1