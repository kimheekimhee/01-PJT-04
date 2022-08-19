import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())


for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    students = list(map(int, input().split()))

    answer = []
    for i in range(1,N+1):
        if i not in students:
            answer.append(str(i))
    
    print('#{} {}'.format(test_case, ' '.join(answer))) 