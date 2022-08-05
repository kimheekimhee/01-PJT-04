import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for i in range(1, T+1):
    N, K = map(int, input().split())
    result = []
    for j in range(1, N+1):
        result.append(j)
    number_list = list(map(int, input().split()))
    for k in number_list:
        result.remove(k)
    print(f'#{i}', *result)
