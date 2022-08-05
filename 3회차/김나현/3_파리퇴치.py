import sys
from pprint import pprint

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for _ in range(1, T + 1):
    max_total = 0
    total = 0
    n, m = map(int, input().split())
    list_ = [list(map(int, input().split())) for _ in range(n)]
    # pprint(list_)
    
    # 가로, 세로의 경우 n - m + 1까지만 for문 돌림
    for x in range(n - m + 1):
        for y in range(n - m + 1):
            if total > max_total:
                max_total = total
            total = 0
            # M 크기의 파리채 : 가로, 세로 M만큼의 면적을 total에 더함
            # y += 1 을 m까지 더해주기
            for j in range(m):
                for i in range(m):
                    total += list_[x + j][y + i]
                    # print(total)
    print('#', _, ' ', max_total, sep='')
    # break