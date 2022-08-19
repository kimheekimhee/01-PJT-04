import sys

sys.stdin = open("_조교의성적매기기.txt")

t = int(input())
hak = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']


for case in range(1, t+1):
    N, K = map(int, input().split()) #학생 수와 평점을 알고 싶은 학생 수
    s_list = []
    
    for _ in range(N):
        mid, final, report = map(int, input().split())
        score = (mid*0.35) + (final*0.45) + (report*0.2) #중간기말과제 총합
        s_list.append(score)

    k_student = s_list[K-1] # 점수를 알고 싶은 k번째 학생의 인덱스부터 구해야한다.
    s_list.sort(reverse=True)# 정렬을 먼저 시키면 결과가 다르게 나온다.
        
    p = N//10 # N명의 학생이 있을 경우 N/10명의 학생들에게 동일한 평점을 부여
    result = s_list.index(k_student) // p
    
    print(f'#{case} {hak[result]}')