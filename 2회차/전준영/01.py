import sys
input=sys.stdin.readline
answer=[]
for _ in range(10):
    input()
    input0=list(map(int,input().split()))
    temp=0
    cnt0=1
    while(True):
        temp=input0.pop(0)
        temp-=cnt0
        if(temp>0):
            input0.append(temp)
        else:
            input0.append(0)
            break
        cnt0+=1
        if(cnt0>5):
            cnt0=1
    answer.append(input0)
cnt=1
for i in answer:
    print('#'+str(cnt),end=' ')
    cnt+=1
    for k in i:
        print(k,end=' ')
    print()

