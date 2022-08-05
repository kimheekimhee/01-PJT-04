import sys

sys.stdin = open("_민석이의과제체크하기.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    people, done = map(int, input().split())
    done_list = list(map(int, input().split()))
    # 전체 수업 들은 사람은 range(1, people + 1)이고 과제를 제출한 사람이 몇명이고 누구인지 정보가 주어져있습니다.
    do_not = []
    for i in range(1, people + 1):
        if i not in done_list:
            do_not.append(i)
            # 그래서 빈 리스트를 만들고 전체를 순회하며 빈 리스트에 낸 사람에 포함되지 않은 사람들을 모아줍니다.
    print(f'#{test}', end = ' ')
    for i in do_not:
        print(i, end = ' ')
    print()