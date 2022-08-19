from cgi import test
import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
for test_case in range(1,T+1) : 
    # 성적
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    N, K = map(int, input().split())

    total_list = []

    for _ in range(N): 
        # 중간, 기말, 과제 
        mid, final, hws = map(int, input().split())
        # 총점 
        total = (mid * 0.35) + (final * 0.45) + (hws*0.2)
        total_list.append(total)
        # [74.6, 92.55000000000001, 88.8, 99.45, 72.35, 85.85000000000001, 96.25, 68.95, 85.5, 85.75]

    # k번째 학생의 인덱스
    k_score = total_list[K-1]
    
    # 내림차순 정렬
    total_list.sort(reverse=True)
    # [99.45, 96.25, 92.55000000000001, 88.8, 85.85000000000001, 85.75, 85.5, 74.6, 72.35, 68.95]
    
    #  N/10 명의 학생들에게 동일한 평점을 부여
    div = N//10
    
    final_k_score = total_list.index(k_score) // div

    print('#{} {}'.format(test_case, grades[final_k_score]))   

