import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for test_case in range(1,T+1) : 
    # 수강생의 수를 나타내는 정수 N , 과제를 제출한 사람의 수를 나타내는 정수 K
    N, K = map(int, input().split())

    #과제를 제출한 사람의 번호 K개가 공백으로 구분되어 주어진다
    project = list(map(int,input().split()))
    
    # 답을 담을 리스트를 생성
    result = []

    for i in range(1, N+1) : 
        if i not in project :
            result.append(i)

    print(f'#{test_case}', end = ' ')
    for i in result:
        print(i, end = ' ')
    print()

