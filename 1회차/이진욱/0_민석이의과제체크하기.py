import sys

sys.stdin = open("_민석이의과제체크하기.txt")


T = int(input())

for t in range(1,T+1):
    N,K = map(int,input().split())
    input_list = list(map(int,input().split()))
    ans_list = [ i for i in range(1,N+1) if not i in input_list   ]

    print( f'#{t} {" ".join(map(str,ans_list))}'  )