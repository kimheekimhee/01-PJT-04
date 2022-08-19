import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for _ in range(1, 1 + T):
    n, k = map(int, input().split())
    submit_list = list(map(int, input().split()))
    print('#', _, ' ', sep='', end='')
    for i in range(1, n + 1):
        if not i in submit_list:
            print(i, end=' ')
    print()