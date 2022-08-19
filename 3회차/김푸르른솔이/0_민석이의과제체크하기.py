import sys

sys.stdin = open("_민석이의과제체크하기.txt")


n = int(input())
li_ = []

for _ in range(1, n+1):
    a, b = list(map(int, input().split()))
    submit = list(map(int, input().split()))
    for i in range(1, a + 1):
        if i not in submit:
            li_.append(i)
print(li_)