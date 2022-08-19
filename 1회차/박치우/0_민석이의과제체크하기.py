import sys

sys.stdin = open("_민석이의과제체크하기.txt")

test_case = int(input())
for i in range(test_case):
    member, suc = map(int,input().split())
    suc_lst = map(int,input().split())
    mem_lst = [i for i in range(1,1+member)]
    for j in suc_lst:
        if j in mem_lst:
            mem_lst.pop(mem_lst.index(j))
    mem_lst.sort()
    for k in mem_lst:
        print(k,end = ' ')
    print()

