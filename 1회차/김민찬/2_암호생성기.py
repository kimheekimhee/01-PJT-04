import sys

sys.stdin = open("_암호생성기.txt")

for i in range(1, 11):
    N = int(input())
    num = list(map(int, input().split())) # 암호 받기
    count = 1

# 문제 이해가 좀 어렵습니다.