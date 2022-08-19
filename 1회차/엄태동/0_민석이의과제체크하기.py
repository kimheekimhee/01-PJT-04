import sys

sys.stdin = open("_민석이의과제체크하기.txt")
T =int(input())
for i in range(T):
    compare=[]
    N,K=map(int, input().split())
    Submit=list(map(int, input().split()))
    for j in range(1,N+1):
        compare.append(j)
    for k in range(K):
        m=0
        while 1:
            if Submit[k] == compare[m]:
                compare.remove(Submit[k])
                break
            else:
                m+=1
    print(f"#{i+1} ",end='')
    print(*compare)