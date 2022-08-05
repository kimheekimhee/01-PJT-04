import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for _ in range(1, T + 1):
    N, K = map(int, input().split())
    students_list = list(map(int, input().split()))
    every_student = list(range(1, N + 1))
    for a in students_list:
        every_student.remove(a)
    every_student.sort()
    print(f'#{_}', end = ' ')
    print(*every_student)