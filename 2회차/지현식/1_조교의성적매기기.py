import sys

sys.stdin = open("_조교의성적매기기.txt")

for test_case in range(1,int(input())+1):
    n, k = map(int, input().split())
    # 성적
    record = ["0", "A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    # 성적 비율
    rate = n // 10
    student = []
    for i in range(1, n + 1):
        mid, end, home = map(int, input().split())
        # 최종점수
        p = mid * 0.35 + end * 0.45 + home * 0.2
        # 우리가 찾아야 할 인원인지 파악
        if i == k:
            # 우리가 찾아야할 인원이라면 data에 점수 저장
            data = p
        student.append(p)
    student = sorted(student, reverse=True)

    # 찾아야할 인원의 인덱스 값 찾기
    find = student.index(data) + 1
    for i in range(1, 11):
        # 인덱스 값이 성적 비율에 맞게 찾는 과정
        if rate * i >= find:
            print(f"#{test_case} {record[i]}")
            break