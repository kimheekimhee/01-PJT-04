import sys

sys.stdin = open("_민석이의과제체크하기.txt")
T = int(input())
for C in range(1, T+1):
    student = []
    N, M = map(int, (input().split()))
    X = input().split()
    for i in range(1, N+1):
        student.append(str(i))
    answer = set(student) - set(X)
    A = sorted(map(int, (answer)))
    print(f'#{C}', *A)