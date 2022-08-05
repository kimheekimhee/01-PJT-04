import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T =int(input())

for tc in range(1, T+1):

    a, b = map(int, input().split())
    data = list(map(int,input().split()))
    result = []

    for i in range(1, a+1):
        if i not in data:
            result