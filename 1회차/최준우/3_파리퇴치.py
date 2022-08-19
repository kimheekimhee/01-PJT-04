import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for test_case in range(T):
    N, M = map(int, input().split()) # N: 파리가 존재하는 영역, M: 파리채 크기
    flies_field = [list(map(int, input().split())) for _ in range(N)]
    temp = 0 # 임시저장 변수
    result = 0 # 제일 많이 잡을 수 있는 파리의 수

    for i in range(0, N-(M-1)): # 파리채의 크기를 감안한 영역까지만 돈다.
        for j in range(0, N-(M-1)):
            for k in range(i, i+M): # 파리채의 크기 만큼 내부 순회한다.
                for l in range(j, j+M):
                    temp += flies_field[k][l] # 파리 수를 더해준다.
            if result < temp: # 이전보다 큰 값이면 result에 넣어준다.
                result = temp
            temp = 0
    print(f'#{test_case+1} {result}') # 출력