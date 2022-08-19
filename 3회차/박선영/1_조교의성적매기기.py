import sys
from pprint import pprint
sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    student = []                       # 전체 학생들의 총점을 저장할 리스트
    for _ in range(n):                 # student 리스트에 전체 학생들의 총점을 저장함
        mid, last, homework = map(int, input().split())
        student.append(mid * 0.35 + last * 0.45 + homework * 0.2)
    ssstudent = student[k-1]           # k번 학생의 총점도 따로 저장해둠
    student.sort(reverse=True)         # 내림차순 정렬
    grade = student.index(ssstudent)   # k번 학생의 등수 저장
    i = 1
    while grade + 1 > (n/10 * i):
        i += 1
    print(f'#{test_case} {grade_list[i-1]}')