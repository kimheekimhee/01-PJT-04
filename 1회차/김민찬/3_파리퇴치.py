import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for _ in range(1, T + 1):
    N, M = map(int, input().split()) # N X M 배열(행열)
    room = [] # 한 칸
    for i in range(N):
        room.append(list(map(int, input().split())))

    room_sum = [] # 네 칸의 합을 저장할 리스트 생성
    for i in range(N - M + 1): # 한 칸 전까지 범위 설정
        for j in range(N - M + 1):
            result = 0
            for k in range(0, M): # 0부터 M - 1까지 더해준다.
                for l in range(0, M):
                    result += room[i + k][j + l] # 행으로 1, 열로 1 더해준다.
            room_sum.append(result)

    print(f'#{_}', max(room_sum)) # max를 사용하지 않으면 합해서 나오는 결과가 다 나온다.
                                  # 최대한 많은 파리를 죽이고자 하기 때문에 max 사용