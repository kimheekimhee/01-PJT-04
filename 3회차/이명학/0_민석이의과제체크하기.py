import sys

sys.stdin = open(
    "C:\\Users\\이명학\\Desktop\\멀티캠퍼스\\01-PJT-04\\3회차\\이명학\\_민석이의과제체크하기.txt")


# 민석이는 교수가 되었고, 이번에 처음으로 맡은 과목에 수강생이 N명이다.

# 민석이는 처음으로 과제를 내었다.

# 그리고 제출한 사람의 목록을 받았다.

# 수강생들은 1번에서 N번까지 번호가 매겨져 있고, 어떤 번호의 사람이 제출했는지에 대한 목록을 받은 것이다.

# 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성하라.

T = int(input())

for _ in range(1, T+1):
    a, b = map(int, input().split())  # 수강생의 수 a, 과제 제출 수 b
    good_student_list = list(map(int, input().split()))  # 과제 제출한 사람의 번호
    student_list = []  # 학생들의 번호
    for i in range(1, a+1):
        student_list.append(i)
    for j in good_student_list:   # good_student_list = [2, 5, 3]
        if j in student_list:  # for문 사용 student_list = [1,2,3,4,5]
            student_list.remove(j)  # J값과 같은 값을 student_list에서 삭제
    print(f'#{_}', *sorted(student_list))  # 제출하지 않은 학생 오름차순으로 출력
