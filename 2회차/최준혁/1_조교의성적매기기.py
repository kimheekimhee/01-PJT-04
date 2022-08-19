# import sys

# sys.stdin = open("_조교의성적매기기.txt")

# N 학생 수, K 학생의 번호
# 학생이 받은 시험 및 과제 점수가 주어짐
# N/10명의 학생에게 동일 평점
# 반영비율 중간고사(35%), 기말고사(45%), 과제(20%)
# (87 * 0.35 + 59 * 0.45 + (88 * 0.2
T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(1, T+1):
    N, K = map(int, input().split()) # N 학생 수, K 학생의 번호 
    total_score = []
    for _ in range(N): # 학생 수 만큼 반복하면서
        mid, final, hws = map(int, input().split())
        total = (mid * 0.35) + (final * 0.45) + (hws * 0.2)
        total_score.append(total) # 학생들의 성적을 추가 
    k_score = total_score[K-1] # k번째 = 3번째 학생
    total_score.sort(reverse=True) # [99.45, 96.25, 92.55000000000001, 88.8, 85.85000000000001, 85.75, 85.5, 74.6, 72.35, 68.95] 
    div = N//10 # 학생 수를 10으로 나눈 몫
    result = total_score.index(k_score) // div 

    print('#{} {}'.format(t, grades[result]))