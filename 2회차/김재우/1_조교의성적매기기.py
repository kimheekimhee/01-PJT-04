import sys

sys.stdin = open("_조교의성적매기기.txt")

'''
 N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점
학생들의 중간, 기말, 과제 점수가 주어지고
학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,
K 번째 학생의 학점을 출력하는 프로그램을 작성하라.
1. N은 항상 10의 배수
'''

T = int(input()) 
for tc in range(1, T + 1): 
    result = []
    N, K = map(int, input().split()) # N 학생 수  K 구하고 싶은 학생의 성적
    for _ in range(N):
        mid, final, project = map(float, input().split()) # 중간 기말 과제 점수를 가져옴
        result.append(int(mid * 0.35 + final * 0.45 + project * 0.20))
        
    result.sort()
    print(result)
        
        

