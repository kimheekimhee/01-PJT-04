import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

for i in range(1, T + 1):
    N, K = map(int, input().split())
    student = []
    record = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    K_score = 0
    for j in range(N):
        li = (list(map(int, input().split())))
        score = (li[0] * 0.35) + (li[1] * 0.45) + (li[2] * 0.2)
        student.append(score)
    K_score += student[K-1]
    student.sort(reverse=True)

    max_record = N // 10
    result = student.index(K_score) // max_record
    print(f'#{i} {record[result]}')

    

  