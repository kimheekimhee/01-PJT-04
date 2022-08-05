import sys

sys.stdin = open("_조교의성적매기기.txt")
#등급을 미리 담아놓은다.
N = int(input())
grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for tc in range(1, N +1):
    numbers, k = map(int, input().split())
    #결과값 받아오기
    result = []
    for _ in range(numbers):
        #중간, 기말, 과제 점수 받아오기
        mid, final, assignment = map(int, input().split())
        #총점 구하기
        total = (mid * 0.35) + (final * 0.45) + (assignment * 0.2)
        #결과값을 리스트에 넣어준다
        result.append(total)

    #점수를 확인하고 싶은 학생 확인해주기 #인덱스로 접근해야하니 -1해줘야한다.
    student = result[k-1]
     # 등급 산출을 위해서 점수가 높은 순서대로 정렬해준다.
    result.sort(reverse = True)
    # 평점 비율 계산을 위한 작업
    average = numbers // 10
    # 최종 등급을 산출하기 위한 작업
    final = result.index(student) // average

    #최종 산출
    print(f"#{tc} {grade[final]}")


         