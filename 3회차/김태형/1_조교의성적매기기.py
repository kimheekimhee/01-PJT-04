# import sys

# sys.stdin = open("_조교의성적매기기.txt")

# 학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때, K 번째 학생의 학점을 출력하는 프로그램을 작성하라

import sys

T = int(input())
score_list = []
for i in range(1,T+1):
    N,K = map(int(sys.stdin.readline().split()))
    for i in range(N):
        stu = list(map(int(sys.stdin.readline().split())))
        stu_score = stu[0]*0.35+stu[1]*0.45+stu[2]*0.2
        score_list.append(stu_score)