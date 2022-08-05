import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for i in range(1, T+1):
    students, pass_ = map(int, input().split())
    pass_li = list(map(int, input().split()))
    fail_li = []
    for student in range(1, students + 1):
        if student in pass_li:
            continue
        else:
            fail_li.append(str(student))
    fail = ' '.join(fail_li)
    print(f'#{i} {fail}')