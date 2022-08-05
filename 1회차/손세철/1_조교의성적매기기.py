import sys

sys.stdin = open("_조교의성적매기기.txt")
# 학점 리스트로 만들어줌
list_ = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for tc in range (1,T+1):
# N,K 입력받는다
    N,K = map(int,input().split())
# 점수 담기위한 score 리스트 초기화
    score = []

# 중간, 기말고사,과제 점수 입력받기 위해 for문 사용
for i in range(N):
    a,b,c = map(int,input().split())
    sum_= (a*0.35) + (b*0.45) + (c*0.2)
    score.append(sum_)
# 구하려는 학생의 점수 K_score에 할당, 총점이 높은 순서대로 내림차순으로 정렬
K_score = score[K-1]
score.sort
result = 0

# 10명에게 동일한 평점 , n//10 계산

same = N // 10
result = score.K_score // same

print("#%d %s" % (tc, score[result]))