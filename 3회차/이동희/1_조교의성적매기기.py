T = int(input())
for tc in range(1, T+1): # 1~ 10 
    students, rank = map(int,input().split()) # 학생수 10명, 2등 학생의 점수 출력
    result = []
    for _ in range(1, students+1): # 학생수에 대해 for문
        scores = list(map(int, input().split())) # 각 학생의 점수 입력
        total = scores[0]*0.35 + scores[1]*0.45 + scores[2]*0.20 # 총점 계산
        result.append(total) # result 리스트에 삽입

    grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    step = students // len(grade) # 하나의 평점에 할당가능한 학생 수

    result_ = [[] for _ in range(students)]
    
    for i in grade: 
        for _ in range(int(step)): 
            max_ = max(result)
            max_idx = result.index(max_)
            result[max_idx] = 0
            result_[max_idx] = i

    print(f'#{tc} {result_[rank-1]}')
