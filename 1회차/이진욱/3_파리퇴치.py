import sys

sys.stdin = open("_파리퇴치.txt")

T=int(input())

for k in range(T):

    N,M=map(int,input().split())
    N_List = [list(map(int, input().split())) for _ in range(N)]

    sum=0
    sum_list=[]
    for a in range(N-(M-1)):
        for b in range(N-(M-1)):
            for c in range(a,a+M):
                for d in range(b,b+M):
                    sum += N_List[c][d]

            sum_list.append(sum)
            sum=0

    max_num = max(sum_list)

    print(f'#{k+1} {max_num}')