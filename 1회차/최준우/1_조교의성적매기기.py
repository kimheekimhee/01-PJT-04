import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] # 등급순으로 저장한 리스트

for test_case in range(T):
    N, K = map(int, input().split()) # N: 학생수, K: 알고싶은 학생번호
    fixed_num = N // 10 # 등급당 제한 인원
    total_score = [] # 총점들을 저장할 리스트
    result = '' # 결과를 저장할 변수
    
    for i in range(N): # 학생 수 만큼 반복
        mid_score, final_score, homework = map(int, input().split()) # 중간, 기말, 과제점수를 입력받는다.
        total_score.append((mid_score * 0.35) + (final_score * 0.45) + (homework * 0.2)) # 비율대로 계산해서 총점리스트에 넣어준다.
    K_score = total_score[K-1] # K번째 학생의 총점을 찾아 저장한다.

    total_score = sorted(total_score, reverse= True) # 총점을 내림차순으로 정렬
    grade = total_score.index(K_score) // fixed_num # 몇번째 평점인덱스에 속할 총점인지
    result = grade_list[grade] # 받는 평점
    
    print(f'#{test_case + 1} {result}') # 출력