# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYJCO4t6cCMDFASv&contestProbId=AV5PwGK6AcIDFAUq&probBoxId=AYJCPZjKcDYDFASv&type=PROBLEM&problemBoxTitle=2%EC%A3%BC%EC%B0%A8&problemBoxCnt=6

import sys

sys.stdin = open("_조교의성적매기기 copy.txt")

T = 10
for t in range(1, 10 + 1):
    N, K = 10, 2 # 10명의 학생 중 2번째 학생의 평점 구하기
    for n in range(10):
        a, b, c = map(int, input().split()) # 중간, 기말, 과제
        total = (a * 35/100) + (b * 45/100) + (c * 20/100) # 총점
        score_list = list(total)
        print(score_list)


