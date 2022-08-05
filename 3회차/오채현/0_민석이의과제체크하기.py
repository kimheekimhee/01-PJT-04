import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for testcase in range(1, T + 1):
    n, k = map(int, input().split())
    student = list(range(1, n + 1))
    sbm = list(map(int, input().split()))
    mis = []
    for s in student:
        if s not in sbm:
            mis.append(s)

    print(f'#{testcase}', *mis)
