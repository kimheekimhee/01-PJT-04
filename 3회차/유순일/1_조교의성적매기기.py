import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())    # 총 테스트 수 입력
grades =['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, T + 1):
    # n = 수강생 수, k = 성적 알고 싶은 학생 번호
    n, k = map(int, input().split())
    
    total_score = []
    
    for _ in range(n):  # n = 수강생만큼 돌아
        mid, final, submit = map(int, input().split())
        total = (mid * 0.35) + (final * 0.45) + (submit * 0.2)
        total_score.append(total)
    
    k_score = total_score[k-1]   # 학생 순번대로의 점수리스트에서 k번째 학생의 점수
    
    total_score.sort(reverse=True)  # 석차를 매길거니 역순정렬
    div = n//10     # n/10명만큼 자를거야.
    k_rank = total_score.index(k_score) // div 
    
       
    print(f'#{tc} {grades[k_rank]}')