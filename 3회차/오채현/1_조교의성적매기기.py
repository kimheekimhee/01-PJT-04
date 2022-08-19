import re
import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for testcase in range(1, T + 1):
    n, k = map(int, input().split())
    students = []
    for i in range(n):
        mid, fin, asn = map(int, input().split())
        total = (mid * 0.35) + (fin * 0.45) + (asn * 0.2)
        students.append(total)

    Ktotal = students[k-1]
    students.sort(reverse=True)

    per = int(n / 10)

    Kgrd = students.index(Ktotal) // per
    print(grade[Kgrd])

    # grd = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))
