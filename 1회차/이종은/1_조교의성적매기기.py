import sys

sys.stdin = open("input (3).txt")

t = int(input())

grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']


for i in range(1, t+1):
    n, m = map(int, input().split())
    result = []
    for j in range(n):
        a, b, c = map(int, input().split())
        sum1 = a*0.35 + b*0.45 + c*0.2
        result.append(sum1)
    
    k_score = result[m-1] #k번째 학생의 인덱스 값 구하기 => 그 학생의 점수

    result1 = sorted(result, reverse=True) #내림차순으로 정렬

    div = n//10 # 동일한 평점 부여하기 때문에 10 나눔

    
    final = result1.index(k_score) // div # 학생 점수가 있는 인덱스를 번호 추출, 그 번호를 학생수로 나누고
    # 예를들어 30명일 경우, 3명씩 같은 등급을 받을 수 있음, k가 3인데, 3번재 학생의 점수가 k-score이고, 그 점수의 인덱스 번호를 구함
    # 근데 인덱스 번호가 3이면 3을 나누기 ? 

    


    print(f'#{i}', grades[final]) # grades 리스트에 그 번호 맞는 값 출력 



        




