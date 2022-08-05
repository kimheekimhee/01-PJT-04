# D2문제-조교의 성적 매기기



# 입력
'''
1. 테스트 케이스 수 T
2. 학생수 N, 학점을 알고 싶은 학생의 번호 K
- N: 10의 배수
- 10 <= N <= 100
- 1 <= K <= N
3. 각각 N명의 학생이 받은 시험 및 과제 점수
'''



# 출력
'''
1. #{해당 테스트케이스} + {k번째 학생의 학점} 
- 총 10개의 평점
- 10개의 평점은 총점(= 중간35% + 기말45% + 과제20%)이 높은 순대로 부여
- N명의 학생이 있을 경우, N/10명의 학생들에게 동일한 평점이 부여됨
- 총점이 같은 학생은 K의 입력값으로 주어지지 않음!!!!
'''



# 코드
import sys

sys.stdin = open("input_text/_조교의성적매기기.txt")

T = int(input())
level = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] 
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    
    # 각 학생의 총점 
    scores = [0] * (N + 1)   # 인덱스: 학생의 번호, 값: 각 학생의 총점
    for num in range(1, N + 1):   # num: 학생의 번호
        middle, final, project = map(int, input().split())   # 중간, 기말, 과제 점수
        score = middle * 0.35 + final * 0.45 + project * 0.2
        scores[num] = score

    # K번째 학생의 평점 구하기
    score_K = scores[K]   # K번째 학생의 점수
    scores.sort(reverse=True)   # 총점에 따라 등수 매기기
    rank = scores.index(score_K)   # K번째 학생의 등수 (0등 ~ (N-1)등)

    print(f'#{test_case} {level[rank // (N // 10)]}')



# 실행시간(메모리:57,032KB, 시간:138ms)