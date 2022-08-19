import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for t in range(1, T+1):
    n, k = map(int,input().split())

    # 과제 제출 안한 사람
    none = [] 
    # 과제 제출 한 사람들
    k_list = list(map(int,input().split()))

    # 수강생 번호대로 반복문
    for p in range(1,n+1):

        # 만약 어떤 수강생이 과제 제출 리스트에 포함되지 않는다면
        if p not in k_list:
            # none 리스트에 추가
            none.append(p)

    print(f'#{t}',*none)