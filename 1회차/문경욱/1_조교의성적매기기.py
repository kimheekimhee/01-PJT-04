import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

# 성적용 리스트 생성
grade_ = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_case in range(1, T+1):
    # 입력값을 받음
    N, K = map(int, input().split())
    score_ = [list(map(int, input().split())) for _ in range(N)]
    
    # 최종 성적 저장용 리스트 생성
    final_score = []
    for i in range(N):
        final_score.append(score_[i][0] * 0.35 + score_[i][1] * 0.45 + score_[i][2] * 0.20)

    # K 번째 학생의 점수를 구함
    check_score = final_score[K-1]
    
    # 최종 성적을 내림차순으로 정렬
    final_score = sorted(final_score, reverse=True)

    # K 번째 학생의 점수를 이용해 등수(인덱스)를 알아냄
    check_idx = final_score.index(check_score)

    # 10명이면 1명씩, 20명이면 2명씩, N명이면 N/10명씩 성적이 나눠짐
    # int(check_idx/(N/10))를 grade_의 등수로 활용

    # 등수 확인용 rank 정함
    rank = int(check_idx/(N/10))
    
    print(f'#{test_case} {grade_[rank]}')
