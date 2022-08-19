import sys

sys.stdin = open("_조교의성적매기기.txt")


t = int(input())

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for testcase in range(1, t+1):
    n, k = map(int,input().split())
    gradingmatch = []

    for i in range(1, n+1):
        m, f, a = map(int,input().split())
        cnt : (m*0.35) + (f*0.45) + (a*0.2)
        gradingmatch.append(cnt)
    print(gradingmatch)