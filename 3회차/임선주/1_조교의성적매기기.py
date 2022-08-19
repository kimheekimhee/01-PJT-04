# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYJCO4t6cCMDFASv&contestProbId=AV5PwGK6AcIDFAUq&probBoxId=AYJCPZjKcDYDFASv&type=PROBLEM&problemBoxTitle=2%EC%A3%BC%EC%B0%A8&problemBoxCnt=6

import sys

sys.stdin = open("_조교의성적매기기 copy.txt")

T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    for n in range(N):
        a, b, c = map(int, input().split())
        total = (a * 35/100) + (b * 45/100) + (c * 20/100)

