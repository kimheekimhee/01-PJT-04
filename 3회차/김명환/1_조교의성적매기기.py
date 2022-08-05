import sys
sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
grade = ['A+','A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for i in range(T):
    N, K = map(int,input().split()) # 학생수, 알고싶은 학생의 번호 
    score_list = []
    for j in range(N):
        m, f, a = map(int,input().split())
        score = (m * 0.35) + (f * 0.45) + (a * 0.2)
        score_list.append(score)
    k_score = score_list[K-1]
    sorted_list = sorted(score_list,reverse=True)
    same = N/10
    for x in sorted_list:
        if x == k_score:
            idx = int(sorted_list.index(x)//same)
    print(f'#{i+1} {grade[idx]}')

