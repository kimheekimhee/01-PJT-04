import sys

sys.stdin = open("_조교의성적매기기.txt")

grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    scores = []
    for i in range(N):
        mid, final, hws = map(int, input().split())
        scores.append((mid * 0.35) + (final * 0.45) + (hws*0.2))
    scoreK = scores[K-1]
    scores.sort(key=lambda x:-x)
    rankOfK = scores.index(scoreK) // (N // 10)

    print('#{} {}'.format(test_case, grades[rankOfK]))