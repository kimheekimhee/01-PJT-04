import sys

sys.stdin = open("_파리퇴치.txt")
sum_=0
Sum_list=[]
T=int(input())
for i in range(T):
    x_=[]
    y_=[]
    N,M=map(int, input().split())
    Matrix=[list(map(int, input().split())) for i in range(N)]
    for delta in range(M):
        for j in range(M):
            x_.append(delta)
            y_.append(j)
    for row in range(N-(M-1)):
        for column in range(N-(M-1)):
            for index in range(len(x_)):
                sum_+=Matrix[row + x_[index]][column + y_[index]]
            Sum_list.append(sum_)
            sum_=0
    print(f"#{i+1} {max(Sum_list)}")
    Sum_list=[]
    sum_=0
    x_=[]
    y_=[]