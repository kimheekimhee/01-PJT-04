import sys

sys.stdin = open("_파리퇴치.txt")

t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    #파리채를 휘두를 수 있는 영역을 2차원 배열로 만든다.
    board = [list(map(int, input().split())) for _ in range(n)]
    # 그냥 n인 경우 인덱스 범위에서 벗어나며
    # n-m의 경우 m의 값이 증가할 수록 이중 for문으로 탐색할 수 있는 범위가 줄어든다.
    no_flapper = n-m+1
    flapper = [] #죽은 파리의 수의 합을 저장할 공간
    
    #파리채 크기만큼 이중 for문으로 탐색을 한다.
    for i in range(no_flapper):
        for j in range(no_flapper):
            sum_ = 0
            for di in range(m):
                for dj in range(m):
                    sum_ += board[i+di][j+dj]
            flapper.append(sum_)
            
    print(f'#{case} {max((flapper))}')