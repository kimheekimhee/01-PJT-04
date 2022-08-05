import sys

sys.stdin = open("_민석이의과제체크하기.txt")

N = int(input())
for i in range(1, N + 1):
    stu1, sub = map(int, input().split())
    sub_num = list(map(int, input().split()))
    
    list1 = []
    for ele in range(1, stu1+1):
        if ele not in sub_num:
            list1.append(ele)
    print(f'#{i}', *list1)        
