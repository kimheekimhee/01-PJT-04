import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T=int(input())

for q in range(1,T+1):
    Z,X=map(int,input().split())#Z학생수 X제출한 수
    C=list(map(int,input().split()))
    a=[]
    for i in range(1,Z+1):
        if i not in C:
            a.append(i)
    print(f'#{q}',*a)