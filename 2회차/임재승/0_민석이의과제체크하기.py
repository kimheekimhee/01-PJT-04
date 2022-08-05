from sys import stdin

stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for i in range(1, T+1):
    answer = []
    N, K = map(int, input().split())
    li = [0] * (N+1)
    K_number = list(map(int, input().split()))
    for j in K_number:
        li[j] = 1
    for x in range(1, len(li)):
        if li[x] == 0:
            answer.append(x)
    print('#{}'.format(i), end=' ')
    print(*answer)