import sys

sys.stdin = open("_조교의성적매기기.txt")

credit = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] # 학점(credit) 리스트 생성
T = int(input())
for i in range(1, T + 1):
    N, K = map(int, input().split()) # 학생 수 = N, 학생의 번호 = K
    student = [] # 학생 리스트 생성
    for j in range(N):
        mid, final, hw = map(int, input().split())
        sum_score = mid * 0.35 + final * 0.45 + hw * 0.20  # 총점 = 중간(35%) + 기말(45%) + 과제(20%)
        student.append(sum_score)
        
    score = student[K - 1]
    student.sort # 틀린 답 # reverse 부분이 정확이 기억이 안 납니다.
    student_ten = student.index(score) // (N // 10)  # 핵심 코드 -> N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여
    student_credit = credit[student_ten]

    print(f'#{i}', student_credit)