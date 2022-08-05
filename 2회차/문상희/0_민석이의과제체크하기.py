import sys

sys.stdin = open("_민석이의과제체크하기.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    people, done = map(int, input().split())
    done_list = list(map(int, input().split()))
    do_not = []
    for i in range(1, people + 1):
        if i not in done_list:
            do_not.append(i)
    print(f'#{test}', end = ' ')
    for i in do_not:
        print(i, end = ' ')
    print()