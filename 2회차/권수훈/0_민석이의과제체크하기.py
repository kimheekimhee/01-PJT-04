import sys

sys.stdin = open("_민석이의과제체크하기.txt")

num = int(input())

for a in range(1,num+1):
    student , ok = map(int,input().split())
    student_ok = list(map(int,input().split()))
    student_no = []

    for i in range(1,student+1):
        if i not in student_ok :
            student_no.append(i)
    print(f'#{a}', *student_no)
