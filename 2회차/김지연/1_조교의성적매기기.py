import sys

sys.stdin = open("_조교의성적매기기.txt")
AtoD = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = []

    for i in range(N):
        sum_ = 0
        score = list(map(int, input().split()))
        sum_ = (score[0]*0.35) + (score[1]*0.45) + (score[2]*0.20)
        result.append(sum_)

    k_score = result[K-1]

    result = sorted(result)
    result = result[::-1]

    same_score = N // 10 # N/10명 학생들에게 동일한 평점
    result_2 = result.index(k_score) // same_score # result_2에 k번째 학생의 순서 저장

    print('#{} {}'.format(tc, AtoD[result_2]))