# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
T = int(input())

for t in range(1, T+1):
    # 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
    N, M = map(int, input().split())
    # 다음 N 줄에 걸쳐 N x N 배열이 주어진다.
    matrix = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []
    

    # 큰 배열 돌기
    for x in range(N-M+1):
        for y in range(N-M+1):
            sum_ = 0
            # 작은 사각형 만들어서 더하기 
            for i in range(x, x+M):
                for j in range(y, y+M):
                   sum_ += matrix[i][j]

            sum_list.append(sum_)
            
    print(f'#{t} {max(sum_list)}')