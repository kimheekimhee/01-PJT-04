import sys

sys.stdin = open("_조교의성적매기기.txt")

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

t = int(input())                                            # t = total test case, n = number of students for the case
                                                            # k = grade for the student
for tc in range(1, t + 1) :
    n, k = map(int, input().split())
    students_grades = []

    for i in range(n) :
        mid, final, assign = map(int, input().split())
        final_grade = (mid * 0.35) + (final * 0.45) + (assign * 0.2)
        students_grades.append(final_grade)

    k_grade = students_grades[k-1]
    students_grades.sort(reverse=True)

    value = n // 10
    result = students_grades.index(k_grade) // value

    print(f'#{tc} {grade[result]}')