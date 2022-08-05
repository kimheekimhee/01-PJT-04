import sys

sys.stdin = open(
    "C:\\Users\\이명학\\Desktop\\멀티캠퍼스\\01-PJT-04\\3회차\\이명학\\_조교의성적매기기.txt")

T = int(input())

score_list = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
for _ in range(1, T+1):
    N, K = map(int, input().split())  # 학생수 N, 알고싶은 학생의 번호 K
    student_score_list = []
    for i in range(N):
        a, b, c = map(int, input().split())  # 중간, 기말, 과제 점수
        total = (a*0.35)+(b*0.45)+(c*0.2)  # 총점을 저장할 total 선언
        student_score_list.append(total)  # 리스트에 삽입

    K_grade = student_score_list[K-1]
    good_student_list = sorted(student_score_list)  # 점수 정렬
    good_student_list = good_student_list[::-1]  # 점수 내림차순 정렬

    div = N//10
    result = good_student_list.index(
        K_grade) // div  # k번째 학생 점수의 인덱스를 div로 나눠준 값을 result에 저장

    print(f"#{_}", score_list[result])
