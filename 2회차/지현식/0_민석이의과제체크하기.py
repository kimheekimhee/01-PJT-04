import sys

sys.stdin = open("_민석이의과제체크하기.txt")

for test_case in range(1, int(input()) + 1):
    n, k = map(int,input().split())
    homework = list(map(int, input().split()))
    answer = []
    for i in range(1, n + 1):
        if i not in answer:
            answer.append(i)
    print(f"#{test_case} {' '.join(map(str,answer))}")