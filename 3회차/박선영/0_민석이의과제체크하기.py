import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    list_ = list(map(int, input().split()))
    origin = [i for i in range(1, n + 1)]
    result = []
    for i in origin:
        if i not in list_:
            result.append(i)
    print(f'#{test_case}', *result)
