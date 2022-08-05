import sys

sys.stdin = open("_민석이의과제체크하기.txt")


T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    N_list = list(map(int, input().split()))
    
    print(f'#{i+1}', end=" ")
    for j in range(1, N+1):
        if j not in N_list:
            print(j, end=" ")
    print()
    