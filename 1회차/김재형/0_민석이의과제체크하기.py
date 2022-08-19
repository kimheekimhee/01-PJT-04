import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
# n명의 수강생 중 과제 낸 사람 k명
# 과제를 안낸 n-k명을 오름차순으로 출력

for t in range(T):
    n, k = map(int, input().split())
    hw = list(map(int, input().split()))
    q = []
    for a in range(n):
        q.append(a+1)
    for i in range(k):
        q.remove(hw[i])
    print(f'#{t+1}', *q)
    