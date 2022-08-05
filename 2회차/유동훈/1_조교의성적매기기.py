import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for i in range(1, T+1):
    N, K = map(int, input().split())
    score = [0]*N
    for j in range(N):
        middle, final, homework = map(int, input().split())
        score[j] = 0.35*middle + 0.45*final + 0.2*homework
   
    K_score = score[K-1]
    score.sort(reverse=True)
    idx = score.index(K_score)
    n = N//10
    print(f'#{i} {grade[idx//n]}')