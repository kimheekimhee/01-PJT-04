#import sys

# sys.stdin = open("_파리퇴치.txt")

T = int(input())

for _ in range(1, T+1):
    N, M = map(int, input().split()) # N = 배열의 크기, M = 파리채의 크기
    N_map = [list(map(int, input().split())) for _ in range(N)]
    fly = 0

    for r in range(N-M+1): # N에 M만큼의 파리채를 옮겨가며 파리의 개수를 담는다
        for c in range(N-M+1):
            sum_value = 0 # 파리의 수 합계를 담을 변수
            for mr in range(M): # 파리채의 크기만큼
                for mc in range(M):
                    sum_value += N_map[r+mr][c+mc] 
            if sum_value > fly: # 파리의 최대값 구하기
                fly = sum_value

            
    print("#{} {}".format(_, fly))

