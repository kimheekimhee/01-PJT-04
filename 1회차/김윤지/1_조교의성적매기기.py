import sys

sys.stdin = open("조교.txt")

t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split(' '))
    students = [] #한번에 리스트로 받으니까 프린트 결과가 이상..리스트 따로 만들자
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for i in range(n): #학생수범위
        mid, fin, repo = map(int, input().split())
        total = (mid * 0.35) + (fin * 0.45) + (repo * 0.20) #총점구해주기
        students.append(total) # 총점을 리스트에 넣자

    k_socre = students[k-1] #k의 점수. 리스트는 0부터니까 1개빼줌
    students.sort(reverse=True) #오름차순으로 정렬하기
    #print(students)
    #k가 어딨는지..어떻게 알지..?
    k_here = students.index(k_socre) #학생들중 k의 인덱스위치 구하기
    #print(k_here)
    #이제 평균구하기..어떻게..?
    k_rank = k_here // (n//10) #먼저 점수분배를 위해 n명을 10으로 나눈 몫 으로 k가 몇등인지 알 수있게 나눠 그 몫을 구함. 
    #print(ttotal)
    k_grade = grade[k_rank] #k의 등수가 grade에서 몇번째인지 구하면 성적나옴.
    print(f'#{tc} {k_grade}')