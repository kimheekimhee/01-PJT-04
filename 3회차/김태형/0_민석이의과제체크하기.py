# 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성하라.

# import sys

# sys.stdin = open("_민석이의과제체크하기.txt")
# input_ = sys.stdin.read()

# T = input_[0]

T = int(input())
stu = []
for i in range(1,T+1):
    N,K = map(int,input().split())
    k=list(map(int,input().split()))
    for i in range(1,N+1):
        stu.append(i)
    

# print("#%d %d" %(i, count_under))