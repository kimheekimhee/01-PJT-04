# import sys

# sys.stdin = open("_민석이의과제체크하기.txt")
T = int(input())
for t in range(1,T+1):
    total, finish = map(int, input().split()) #수강생 수, 제출한 사람 수
    finish_lst = []
    notfinist_lst = []
    finish_lst = list(map(int, input().split()))
   
    for i in range(1, total+1):
        if i not in finish_lst:
            notfinist_lst.append(i)
    notfinist_lst.sort()
    print(f'#{t}', *notfinist_lst)

 
