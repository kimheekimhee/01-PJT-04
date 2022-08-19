import sys

sys.stdin = open("_민석이의과제체크하기.txt")

a = int(input())

for i in range(a):
    student = []
    b, c = map(int, input().split())
    good_stu = [map(int, input().split()) for i in range(b)]
    for i in range(1, b + 1):
        student.append(i)
        if good_stu in student:
            student.pop(good_stu)


    print(f'{i+1} {student}, end = ""')