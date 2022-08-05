import sys

sys.stdin = open("_민석이의과제체크하기.txt")
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T+1):
    n ,k = map(int, input().split())
    report = set(map(int, input().split()))
    lst = []
    for i in range(1, n+1):
        if i not in report:
            lst.append(i)
    print(f'#{test_case}',end =' ')
    print(*lst)