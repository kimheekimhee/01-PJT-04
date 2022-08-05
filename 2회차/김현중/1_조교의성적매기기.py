import sys
import heapq
sys.stdin = open("_조교의성적매기기.txt")
input = sys.stdin.readline

T = int(input())
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for test_case in range(1, T+1):
    N, K = map(int, input().split())                # 학생수 N, K번째 학생의 학점
    scores = {}
    score_lst = []
    for i in range(1, N+1):
        mid_term, final_term, report = map(int, input().split())
        score = round(mid_term *(0.35) + final_term*(0.45) + report*(0.2), 2)
        score_lst.append(score)
        scores[i] = scores.get(i, score)
    score_lst.sort(reverse=True)
    print(f'#{test_case} {grade[score_lst.index(scores[K])//int(N/10)]}')