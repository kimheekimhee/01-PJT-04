import sys

sys.stdin = open("_조교의성적매기기.txt")

g = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())
    grade = []
    score = {}
    idx = 0

    for j in g:
        for l in range(n // 10):
            # 학생의 수만큼 등급을 배로 늘려준다.
            grade.append(j)

    for j in range(1, n + 1):
        mid, final, hw = map(int, input().split())
        score[j] = (mid * 0.35) + (final * 0.45) + \
            (hw * 0.2)   # 성적을 학생 수만큼 퍼센트를 계산하여 더해준다

    # 성적을 기준으로 점수를 정렬한다
    score = sorted(score.items(), key=lambda x: (-x[1], x[0]))

    for j in range(n):
        # 원하는 학생의 번호가 점수 튜플의 첫 번째 인덱스의 값과 같다면
        if k == score[j][0]:
            # 점수 튜플의 인덱스를 구하여 idx로 저장한다
            idx = score.index(score[j])

    # 등급 리스트에서 인덱스가 idx인 등급을 출력한다
    print(f'#{i} {grade[idx]}')
