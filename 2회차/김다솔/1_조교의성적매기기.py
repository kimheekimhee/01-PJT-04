import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
for tc in range(1, T+1):
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'][::-1]
    #print(grades)
    scores = []

    N, K = map(int, input().split())
    for i in range(N):
        m, f, a = map(int, input().split())
        score = m*0.35 + f*0.45 + a*0.2
        scores.append(score)

    K_score = scores[K-1]
    # print(K_num)
    scores.sort()
    # print(scores)      
    std = N // 10
    K_grade = scores.index(K_score) // std
    
    print(f'#{tc} {grades[K_grade]}')