import sys
from zipfile import ZIP_MAX_COMMENT

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    D = list(map(int, input().split()))
    print(a, b, D)
    result = []
    for i in range(1, a + 1):
        if i not in D:
            result.append(i)
    print(f'#{test_case}', *result)