import sys

sys.stdin = open("_조교의성적매기기.txt")
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    score_list = []
    for a in range(N):
        student_score = list(map(int, input().split()))
        score_list.append((student_score[0]/100*35) + (student_score[1]/100*45) + (student_score[2]/100*20))
    search_score = score_list[K - 1]
    score_list.sort(reverse = True)
    result = score_list.index(search_score)
    AtoD = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(1, 11):
        if result < i * N / 10:
            print(f'#{_ + 1} {AtoD[i - 1]}')
            break