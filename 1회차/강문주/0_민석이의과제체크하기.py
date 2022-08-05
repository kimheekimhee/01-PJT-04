import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())


for test_case in range(1, T + 1):
    total, present = map(int, input().split())
    present_list = list(map(int, input().split()))
    students = []

    for i in range(1, total+1):
        if i not in present_list:
            students.append(i)


    print(f'#{test_case}',*students)