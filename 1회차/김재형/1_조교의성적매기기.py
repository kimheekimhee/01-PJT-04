import sys

sys.stdin = open("_조교의성적매기기.txt")

# 총 테스트 케이스
# T = int(input())

# 학생수, k번쨰 학생
# for t in range(T):
n, k = map(int, input().split())
# 점수 받는 통
score = []
# n명의 학생의 성적과 과제점수를 받는다.
for i in range(n):
    s = list(map(int, input().split()))
    score.append(s)
    # 첫 번째 열은 35%, 두 번쨰 열은 45%, 3 번쨰는 20%
score2 = [[],[],[]]
rank = [] 
r = []
hak = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
m = n // 10
# 열행
for i in range(3):
    p =[0.35, 0.45, 0.2]
    for j in range(n):
        # score2에 각각 퍼센트지 한거 저장
        score2[i].append(score[j][i] *p[i])
        # 그럼 이제 각 점수를 다 더해서 순서대로 나열하고 학점을 부여하고 k번째 점수의 학점 출력
for i in range(n):
    sum_ = 0
    for j in range(3):
        sum_ += score2[j][i]
        rank.append(round(sum_,2))
    r.append(rank[i+2])
r.sort(reverse=True)

# 비율에 맞춰서 점수에 학점 부여해야 하는데 어떻게 하지...

 