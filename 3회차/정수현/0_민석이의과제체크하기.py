import sys

sys.stdin = open("_민석이의과제체크하기.txt")
input = sys.stdin.readline
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))
    print(f'#{t}', end=' ')
    for i in range(1, N+1):
        if i in submit:
            continue
        print(i, end = ' ')
    print()