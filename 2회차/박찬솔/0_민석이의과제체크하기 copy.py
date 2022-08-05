import sys

sys.stdin = open("_민석이의과제체크하기.txt")
t = int(input())
for j in range(t):
    n, k = map(int, input().split())
    a= input()
    a = a.split()
    non = []
    for i in a:
        non.append(int(i))
    c = []
    for i in range(1, n+1):
        if i not in non:
            c.append(i)
    c.sort()
    print(f'#{i} {j + i}', end = ' ')
    for i in c:
        print(i, end = ' ')
    print()
# k =  과제 제출한 사람 번호
# n =  수강생의 수
# non = 제출하지 않은 사람의 번호