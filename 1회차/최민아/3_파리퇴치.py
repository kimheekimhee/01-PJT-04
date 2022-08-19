import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())                                    # 테스트케이스 개수

for test_case in range(1, T+1):
    N, M = map(int, input().split())                # 영역 크기, 파리채 크기

    arr = []                                        # 해당 영역에 존재하는 파리 수
    for i in range(N):
        arr.append(list(map(int, input().split()))) # 2차원 배열

    fly_kill = []                                   # 한 번에 죽일 수 있는 파리 수
    for i in range(N-M+1):                          # 영역 범위(파리채 왼쪽 위 좌표 기준)
        for j in range(N-M+1):                      # 영역 범위(파리채 왼쪽 위 좌표 기준)
            kill = 0                                # 파리 수
            for mi in range(M):                     # 파리채 범위
                for mj in range(M):                 # 파리채 범위
                    if i+mi < N and j+mj < N:       # 파리채가 영역을 벗어나지 않으면
                        kill += arr[i+mi][j+mj]     # 해당 영역 파리 수 더함
            fly_kill.append(kill)

    print(f'#{test_case} {max(fly_kill)}')          # 최대 죽은 파리 수 출력