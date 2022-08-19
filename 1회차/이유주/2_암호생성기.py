import sys

sys.stdin = open("_암호생성기.txt")

T = int(input())
number = list(map(int, input().split()))
for i in range(8):
    number[i] = number[i] - (i+1)
    if number[i] <= 0:
        number[i] == 0
        print(f'#{T} {number}')