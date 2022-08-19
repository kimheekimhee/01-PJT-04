import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
T=int(input())
for i in range(T):
    N, K= map(int, input().split())
    Matrix=[list(map(int, input().split())) for i in range(N)]
    Length=[]
    Length_list=[]
    cnt=0
    Right_place=0
    ForCount=False
    for row in range(N):
        for column in range(N):
            if Matrix[row][column] ==1:
                cnt+=1
                ForCount=True
                if column == N-1:
                    Length.append(cnt)
                    cnt=0
            elif Matrix[row][column]==0:
                if ForCount==True:
                    Length.append(cnt)
                    cnt=0
                    ForCount=False
                elif ForCount ==False:
                    pass
        Length_list.append(Length)
        Length=[]
    for check1 in range(len(Length_list)):
        for check2 in range(len(Length_list[check1])):
            if Length_list[check1][check2] ==K:
                Right_place+=1
    Length_list=[]
    Length=[]
    ForCount=False
    for column in range(N):
        for row in range(N):
            if Matrix[row][column] ==1:
                cnt+=1
                ForCount=True
                if row == N-1:
                    Length.append(cnt)
                    ForCount=False
                    cnt=0
            elif Matrix[row][column]==0:
                if ForCount==True:
                    Length.append(cnt)
                    cnt=0
                    ForCount=False
                elif ForCount ==False:
                    pass
        Length_list.append(Length)
        Length=[]
    for check1 in range(len(Length_list)):
        for check2 in range(len(Length_list[check1])):
            if Length_list[check1][check2] == K:
                Right_place+=1
    print(f'#{i+1} {Right_place}')
