import sys

sys.stdin = open("_민석이의과제체크하기.txt")
answer = []
N = int(input())
for tc in range(1, N+1):
    numbers, pass_number = map(int, input().split())
    pass_ = list(map(int, input().split()))
    for i in range(1, numbers+1):
        if i not in pass_:
            answer.append(i)

    print(f"#{tc} {answer}")


       