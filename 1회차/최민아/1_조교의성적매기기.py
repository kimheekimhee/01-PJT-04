import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())                                              # 테스트케이스 개수

for test_case in range(1, T+1):
    N, K = map(int, input().split())                          # 학생 수, 알고싶은 학생 번호

    score = []                                                # 번호 순 총점 리스트
    for i in range(N):
        mid, end, project = map(int, input().split())         # 중간, 기말, 과제 점수
        score.append((mid*0.35)+(end*0.45)+(project*0.2))     # 총점 계산 후 추가
    sort_score = sorted(score, reverse=True)                  # 성적 순 총점 리스트

    grade_list = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0'] # 평점 종류
    grade = ''                                                # 학생이 받을 평점
    for j in sort_score:                                      # 성적 순 총점이
        if j == score[K-1]:                                   # K번 학생의 총점과 같으면
            grade = grade_list[sort_score.index(j)//(N//10)]  # 등수(성적 순 인덱스)와 비율에 따라 평점을 구함 

    print(f'#{test_case} {grade}')                            # K번 학생의 평점 출력