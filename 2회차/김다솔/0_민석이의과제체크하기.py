import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    N_list = set(range(1, N+1))
    NK = set(map(int, input().split()))
    no_asgmt = list(N_list - NK)
    print(f'#{tc}', end=' ')
    print(*no_asgmt)