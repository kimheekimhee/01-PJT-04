import sys

sys.stdin = open("_민석이의과제체크하기.txt")
T=int(input())
for i in range(1,T+1):
    a, b = map(int, input().split())
    number = list(map(int, input().split()))
    result = [ ]
 
    for j in range(1,a+1):
        if j not in number :
            result.append(j)
    print(f'#{i}', *result)