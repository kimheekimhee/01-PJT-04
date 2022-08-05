# import sys

# sys.stdin = open("_파리퇴치.txt")

T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())

    # arr 입력받기
    arr = [list(map(int, input().split())) for _ in range (n)]
    # mXm에서의 sum 저장할 변수 초기화
    sum_ = 0
    # sum_ 값 저장할 리스트 초기화
    sum_list = []

    # nXn 순회
    for i in range(n-m+1):
        for j in range(n-m+1):
            # mXm 순회
            for k in range(i, i+m):
                for l in range(j, j+m):
                    # sum_에 합 값 
                    sum_ += arr[k][l]
            # sum_list에 합 값 추가하기
            sum_list.append(sum_)
            # 합 값 초기화
            sum_ = 0
    print(f'#{t} {max(sum_list)}')