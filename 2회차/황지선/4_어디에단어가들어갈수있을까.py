T = int(input())

for t in range(1, T+1):
    # 테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
    N, K = map(int, input().split())
    # 테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
    # 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다. 흰 부분에 단어 쓸수 있음
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 3자리 수만 들어갈 수 있는 것인지 확인
    count = 0

    # 행돌기!
    for x in range(N):
        # 행마다 0의 개수 세고 저장할 변수
        sum_0 = 0   
        for y in range(N):
            if matrix[x][y] == 1:
                sum_0 += 1

                # 3자리 이상이 되면 안되기 때문에
                if y == N-1 and sum_0 == K:
                    count += 1

                elif y < N-1 and sum_0 == K:
                    if matrix[x][y+1] != 1:
                        count += 1
            
            else:
                sum_0 = 0

    # 열돌기!
    for y in range(N):
        # 행마다 0의 개수 세고 저장할 변수
        sum_0 = 0   
        for x in range(N):
            if matrix[x][y] == 1:
                sum_0 += 1

                # 3자리 이상이 되면 안되기 때문에
                if x == N-1 and sum_0 == K:
                    count += 1

                elif x < N-1 and sum_0 == K:
                    if matrix[x+1][y] != 1:
                        count += 1
            
            else:
                sum_0 = 0


    print(f'#{t} {count}')


    # 가로 세로 전부 돌아야함!