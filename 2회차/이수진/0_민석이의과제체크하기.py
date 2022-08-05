import sys

sys.stdin = open("_민석이의과제체크하기.txt")

tc = int(input())
for t in range(tc):
    n,k=map(int, input().split())
    students=set(i for i in range(1,n+1))
    submitted=set(map(int, input().split()))
    print(f'#{t+1}',*list(sorted(students-submitted)))