import sys

sys.stdin = open("_조교의성적매기기.txt")

for test_case in range(1,int(input())+1):
    n, k = map(int, input().split())
    record = ["0", "A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    rate = n // 10
    student = []
    for i in range(1, n + 1):
        mid, end, home = map(int, input().split())
        p = mid * 0.35 + end * 0.45 + home * 0.2
        if i == k:
            data = p
        student.append(p)
    student = sorted(student, reverse=True)

    find = student.index(data) + 1
    for i in range(1, 11):
        if rate * i >= find:
            print(f"#{test_case} {record[i]}")
            break