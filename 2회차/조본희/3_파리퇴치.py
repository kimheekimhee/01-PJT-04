import sys

sys.stdin = open("_파리퇴치.txt")
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    deadflies = []

    for i in range(N-(M-1)):                        
        for j in range(N-(M-1)):
            temp = 0

            for k in range(M):
                temp += sum(flies[i+k][j:j+(M)])    #range에 대한 조건문이 많아서 로직을 짜는데 시간이 좀 걸렷다.
                                                    #규칙만 찾으면 구현 자체는 쉬운 문제인듯.
            deadflies.append(temp)

    print(f'#{test_case} {max(deadflies)}')