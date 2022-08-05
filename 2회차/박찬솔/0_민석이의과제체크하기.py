import sys

sys.stdin = open("_민석이의과제체크하기.txt")
# 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성
t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split()) # n = 1, k = 2
    data = list(map(int,input().split()))
    non = []
    # 오름차순 정렬 sorted, 중복이 없으므로 set는 쓰지 않음
    for j in range(1, n+1):
        if j not in data:
            non.append((j))

print(f'#{i}'.format(t), end=' ')

# k =  과제 제출한 사람 번호
# n =  수강생의 수
# non = 제출하지 않은 사람의 번호