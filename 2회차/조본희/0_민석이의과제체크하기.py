import sys
sys.stdin = open("_민석이의과제체크하기.txt")
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    students = []
    delstudents = list(map(int, input().split()))

    for i in range(N):
        students.append(i+1)

    for j in range(K):
        students.remove(delstudents[j])
        
    print(f'#{test_case} {" ".join(map(str, students))}') #f스트링에서 리스트 대괄호 빼고 출력하는 법을 저번주 모의고사때 배웠다.