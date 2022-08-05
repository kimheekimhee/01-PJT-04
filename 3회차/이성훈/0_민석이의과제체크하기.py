import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for j in range(1,T+1):
    print(f'#{j}', end = ' ')
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    k_list = []

    N_list = {}
    # N = 수강생의 수
    # K = 제출한 사람의 수
    # L = 제출한 사람 목록

    for i in range(1,N+1):
        N_list[i] = 0

    for i in L:
        N_list[i] = 1

    for i in N_list:
        k_list.append(i)

    for i in range(1, N+1):
        if N_list[i] == 0:
            print(k_list[i-1], end = ' ')
    print()


