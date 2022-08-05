import sys
input=sys.stdin.readline
array=[0]*4
answer=[1]*10
cnt=0
for _ in range(10):
    input()
    input0=input()
    array.clear()
    array=[0]*4
    for i in input0:
        if(i=='('):
            array[0]+=1
        elif(i=='['):
            array[1]+=1
        elif(i=='{'):
            array[2]+=1
        elif(i=='<'):
            array[3]+=1
        elif(i==')'):
            array[0]-=1
            if(array[0]<0):
                answer[cnt]=0
        elif(i==']'):
            array[1]-=1
            if(array[1]<0):
                answer[cnt]=0
        elif(i=='}'):
            array[2]-=1
            if(array[2]<0):
                answer[cnt]=0
        elif(i=='>'):
            array[3]-=1
            if(array[3]<0):
                answer[cnt]=0
    cnt+=1
for k in array:
    if(k!=0):
        answer[cnt]=0
cnt=1    
for j in answer:
    print('#'+str(cnt),j)
    cnt+=1