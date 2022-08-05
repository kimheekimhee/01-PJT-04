import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for i in range(T):
    number, assign = map(int, input().split())
    assign_list = set(map(int, input().split()))
    whole_list = set(range(1, number + 1))
    no_assign = whole_list - assign_list
    print(f'#{i + 1}', end = ' ')
    for j in list(no_assign):
        print(j, end = ' ')
    print()