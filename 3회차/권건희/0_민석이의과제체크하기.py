import sys

sys.stdin = open("_민석이의과제체크하기.txt")
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    list_=[]
    s=list(map(int,input().split()))
    for i in range(1,N+1):
        if i not in s:
            list_.append(i)
    list_.sort()        
    print(f"#{_+1}",*list_)    