import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for tc in range(1, T + 1):
    C, N = map(int, input().split())
    clear_ = list(map(int, input().split()))
    my_list = []
    for i in range(1, C+1):
        if i not in clear_:
            my_list.append(i)

    print(f'#{tc}', end = ' ')
    print(*my_list)
