import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
result=[]
for test_case in range(1, T + 1):
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    for i in range(1,n+1):
        result.append(i)
    for i in range(len(x)):
        result.remove(x[i])
    print(f'#{test_case}',end=' ')
    for i in result:
        print(i,end=' ')
    print()
    result=[]