from ast import iter_fields
import sys

# sys.stdin = open("_민석이의과제체크하기.txt")

t = int(input())
for test in range(t):
    total_set = set()
    submit_set = set()
    total, submit = map(int,input().split())
    for num in range(1,total+1):
        total_set.add(num)
    submit_lst = list(map(int,input().split()))
    for num in submit_lst:
        submit_set.add(num)
    print(f'#{test+1} ',end='')
    for result in total_set - submit_set:
        print(result,end=' ')
    print()