# import sys

# sys.stdin = open("_민석이의과제체크하기.txt")

N = int(input())

for i in range(1,N+1):
    a,b = map(int,input().split())
    data = list(map(int,input().split()))
    result = []

    for j in range(1,a+1):
        if j not in data:
            result.append(j)

    print(f'#{i}', *result)

