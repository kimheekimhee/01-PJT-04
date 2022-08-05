# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYJCO4t6cCMDFASv&contestProbId=AWVl3rWKDBYDFAXm&probBoxId=AYJCPZjKcDYDFASv&type=PROBLEM&problemBoxTitle=2%EC%A3%BC%EC%B0%A8&problemBoxCnt=6

import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for t in range(1, T + 1):
    M, N = map(int, input().split()) # m은 수강생 수, n은 과제 제출한 사람 수
    # 수강생 번호 리스트 안에 넣기
    students = list(range(1, M + 1))
# 과제 제출한 사람 번호 제거하기
    o_ss = list(map(int, input().split())) # 과제 제출한 사람 번호
    x_ss = list(set(students) - set(o_ss)) # 과제 미제출자 번호
# 과제 미제출자 번호 뽑기
    for n in range(M - N):
        
        print(f'#{t} {x_ss[n]}')


# 조건문 사용
T = int(input())

for t in range(1, T + 1):
    M, N = map(int, input().split()) # M : 수강생 수, N : 과제 제출한 사람 수
    students = list(range(1, M + 1)) # 수강생 번호 리스트
    yes = list(map(int, input().split())) # 제출자 번호
    no = [] # 미제출자 담을 빈 리스트

    for i in range(1, M + 1):
        if i not in yes:
            no.append(i)

