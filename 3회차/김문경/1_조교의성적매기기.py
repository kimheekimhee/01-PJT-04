import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

for test_case in range(T):
    N, K = map(int, input().split())
    student_dict = {}
    # N은 학생 수, K는 학점 알고싶은 학생의 번호
    for student in range(1, N + 1):
        mid, final, assign = map(int, input().split())
        total = mid * 0.35 + final * 0.45 + assign * 0.2
        student_dict[student] = total
    # 딕셔너리에 데이터 다 넣고 내림차순 정렬
    new_student_dict = sorted(student_dict.items(), key = lambda x : -x[1])
    # 순서를 정렬하면 리스트 안에 튜플로 구성되고 N이 몇번째 인덱스에 있냐를 구할 수 있음
    grade_index = 0
    # 몇 등인지 찾는 반복문
    for i in range(len(new_student_dict)):
        if new_student_dict[i][0] == K:
            grade_index = i + 1
            break
    # N명에 따른 성적 구간 나누기
    grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    R = N / 10 # 항상 10단위로 나뉘니까 N이 몇명이 들어오든 10으로 나눠서 계산
    # 만약 20명 중에서 7등이라면
    grade = grade_index / R
    # R= 20 / 10 = 2, K / R 의 몫은 3(소수점은 버림 처리)
    print(f'#{test_case + 1}', grade_list[result - 1])
