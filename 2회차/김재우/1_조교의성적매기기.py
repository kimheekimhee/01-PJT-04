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
point = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']                # 학점 리스트
for tc in range(1, T + 1): 
    result = []                                                      # 학생들 총점을 모아둘 리스트
    N, K = map(int, input().split())                                 # N 학생 수  K 구하고 싶은 학생의 성적
    for _ in range(N):
        mid, final, project = map(int, input().split())              # 중간 기말 과제 점수를 가져옴
        result.append(mid * 0.35 + final * 0.45 + project * 0.20)    # 점수 비율별로 가져와서 result에 append
    
    student = result[K-1]                                            # 구하려는 학생의 인덱스 위치로 , 점수를 기억
    result.sort(reverse=True)                                        # sort 이용해서 정렬, 단 reverse=True 이용해서 큰 순서대로 출력해줌
    # 학점 리스트와 인덱스 위치를 같게 해준다
    
    grade = N // 10                                                  # 평점은 학생수 / 10으로 부여될 수 있음!
    student_score = result.index(student) // grade                   # K 학생의 학점 구하기 result의 인덱스에서 student 값을 저장한 위치를 찾고 평점을 나눠준다
    # 만약 학생 수가 30명이면 같은 학점을 받는 학생은 grade에 의해서 3명이 된다
    
    '''
    학점이 부여되는 로직을 생각해보면 이렇게 이루어진다!
    0 // 3 = 0  
    1 // 3 = 0 
    2 // 3 = 0 
    3 // 3 = 1 
    4 // 3 = 1
    5 // 3 = 1
    6 // 3 = 2
    7 // 3 = 2
    8 // 3 = 2 
    '''

    print(f'#{tc} {point[student_score]}') # 따라서 result의 인덱스 위치와 point의 인덱스 위치를 같게 만들어주는 것이다!


    
        
        

