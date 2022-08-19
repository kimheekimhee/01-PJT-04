import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for t in range(1,T+1):
    student = set() # 학생은 1부터 1씩 증가하는 식으로 표현이 되어 있고
    # 과제를 제출한 학생들도 번호로 되어 있었다. 
    # 그래서 값에는 중복이 없어서 set를 사용해도 문제가 없었고, 
    # 두 집합의 차를 이용하면 바로 풀릴거 찾아서 set을 사용했습니다.
    N, K = map(int,input().split())
    pass_student = set(map(int, input().split()))# 과제 제출한 학생들
    for stu in range(1,N+1):
        student.add(stu)
    print(f"#{t}", end=" ")
    print(*(student ^ pass_student)) # 강사님이 알려주신 너무 소중한(편한) * 방법

