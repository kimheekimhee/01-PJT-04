# 학점은 상대평가로 주어지며 총 10개의 평점이 있다
# A+ A0 A- B+ B0 B- C+ C0 C- D0
# 학점은 학생들이 응시한 중간/기말고사 점수 결과 및 과제 점수 반영
# 총점 = 중간고사(35%) + 기말고사(45%) + 과제(20%)
# 10개의 평점을 총점이 높은 순서대로 부여
# 각각의 평점은 같은 비율로 부여할 수 있다
# 예 : N명의 학생이 있을 경우 N/10명의 학생들에게 동일한 평점 부여

# 첫 줄에 총 테스트 케이스의 개수 T가 주어진다
# 다음 줄부터 각 테스트 케이스가 주어진다
# 첫 번째 줄은 학생수 N과 학점을 알고 싶은 학생의 번호 K
# 두 번째 줄부터 각각의 학생이 받은 시험 및 과제 점수

# 출력 예시
#1 A-
#2 C-
#3 C0
#4 A-
#5 C0
#6 A-
#7 C+
#8 C+
#9 B0
#10 A0

import sys
sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
grade = ('A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0')

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    scoreList = []
    
    for _ in range(n):
        num1, num2, num3 = map(int, input().split())
        scoreList.append(num1 * 0.35 + num2 * 0.45 + num3 * 0.2)
    #* k번 학생의 점수(k번째 학생의 인덱스)
    k_score = scoreList[k - 1]

    scoreList.sort(reverse = True)

    div = n // 10
    final = scoreList.index(k_score) // div
    print('#{} {}'.format(tc, grade[final]))