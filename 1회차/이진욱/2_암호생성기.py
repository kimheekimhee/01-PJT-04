import sys

sys.stdin = open("_암호생성기.txt")


for i in range(10):

    t = int(input())
    N_list = list(map(int,input().split()))
    start = 1
    while 0 not in N_list:
        if start >5:
            start = 1
        N_list.reverse()
        num = N_list.pop()
        N_list.reverse()
        if (num-start) <= 0:
            N_list.append(0)
            print(f'#{t} {" ".join(map(str,N_list))} ')
            break
        N_list.append(num-start)
        start+=1





