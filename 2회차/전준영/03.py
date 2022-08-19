import sys
input=sys.stdin.readline
answer=[]
metrix=[]
column=[]
temp=[]
T=int(input())
for i in range(T):
    an=0
    input0=list(map(int,input().split()))
    metrix.clear()
    for k in range(input0[0]):
        temp.clear()
        temp=list(map(int,input().split()))
        an=temp[0]*0.35+temp[1]*0.45+temp[2]*0.2
        metrix.append(an)
    an=metrix[input0[1]-1]
    cnt=1
    for j in metrix:
        if an<j:
            cnt+=1
    temp_int=input0[0]/10
    count=0
    while(temp_int<cnt):
        temp_int+=input0[0]/10
        count+=1
    if(count==0):
        answer.append('A+')
    elif(count==1):
        answer.append('A0')
    elif(count==2):
        answer.append('A-')
    elif(count==3):
        answer.append('B+')
    elif(count==4):
        answer.append('B0')
    elif(count==5):
        answer.append('B-')
    elif(count==6):
        answer.append('C+')
    elif(count==7):
        answer.append('C0')
    elif(count==8):
        answer.append('C-')
    elif(count==9):
        answer.append('D')
cnt=1
for j in answer:
    print('#'+str(cnt),j)
    cnt+=1
