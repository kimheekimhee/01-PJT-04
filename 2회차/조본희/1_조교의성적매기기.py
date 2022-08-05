import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    score = []
    for i in range(N):
        a, b, c = map(int, input().split())
        score.append(a*35 + b*45 + c*20) #반영비율 바로 계산해서 넣어버리기

    mult = N // 10  # 학생 수에따라 'A+'등 각각 mult개씩 넣기 위한 변수
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    
    result = [''] * N  
    for i in range(10):
        for j in range(mult):
            idx = score.index(max(score))   #가장 성적이 높은 학생순으로 grade를 넣어준다
            result[idx] = grade[i]
            score[idx] = -1                 #해당 학생의 점수를 -1로 교체함으로 인해 다음 루프때 다음 최대값이 잡히도록 한다.
    print(f'#{test_case} {result[K-1]}')
