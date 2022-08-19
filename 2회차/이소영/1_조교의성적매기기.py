t = int(input())
score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] # 10개의 점수 등급 리스트

for tc in range(1, t+1):
    n, k = map(int, input().split()) # n = 학생의 수 k = 점수를 확인할 학생의 번호
    grade = []
    for _ in range(n):
        a, b, c = map(int, input().split()) # a = 중간 b = 기말 c = 과제
        sumscore = (a * 0.35) + (b * 0.45) + (c * 0.2)
        grade.append(sumscore)

    k_score = grade[k-1] # 학생 k의 점수
    grade.sort(reverse=True)

    value = n // 10
    result = grade.index(k_score) // value

    print("#%d %s" % (tc, score[result]))