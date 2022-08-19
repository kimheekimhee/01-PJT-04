import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for tc in range(1,T+1):
    # 행렬로 풀이 이렇게 푸니까 런타임에러
    # matrix = [list(map(int, input().split())) for a in range(T)]
    # student_num = [] # 행렬의 그 학생의 총 번호 명단
    # for b in range(1, matrix[0][0]+1):
    #     student_num.append(b)
    #     c = matrix[1] # 제출한 학생들의 번호 명단
    # result = [] # 제출 안한 학생들의 번호 명단
    # for b in range(1, matrix[0][0]+1):
    #     if b not in c:
    #         result.append(b)
    
    # print(f"#{tc} {' '.join(map(str,result))}")
    # N 총번호 명단, K는 제출한 학생들의 번호 명단
    N, K = map(int, input().split())

    # 제출한사람의 번호 명단
    c = list(map(int,input().split()))

    # 제출 안한 학생들의 번호 명단
    result = []
    for b in range(1, N+1):
        if b not in c:
            result.append(b)
    
    print(f"#{tc} {' '.join(map(str,result))}")

    
    
        