import sys
from pprint import pprint

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for _ in range(1, T + 1):
    n, k = map(int, input().split())
    list_ = [list(map(int, input().split())) for _ in range(n)]
    total = 0
    # pprint(list_)
    for x in range(n):
        row_count = 0
        col_count = 0
        for y in range(n):
            # 가로
            if list_[x][y] == 1:
                row_count += 1
            else:
                if row_count == k:
                    total += 1
                row_count = 0
            # 세로
            if list_[y][x] == 1:
                col_count += 1
            else:
                if col_count == k:
                    total += 1
                col_count = 0
        if row_count == k:
            total += 1
        if col_count == k:
            total += 1
    print('#', _, ' ', total, sep='')
