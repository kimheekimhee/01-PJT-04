from dataclasses import replace
import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int , input().split())

    array = [list(map(int, input().split())) for _ in range(N)] # 파리가 존재하는 배열
    result = []                                                 # 파리채에 잡힌 파리 수
    sum_ = 0                                                    # 파리 수 더해줄 변수
    for i_array in range(N-(M-1)):                              # 전체 범위 (M-1) 해주는 이유 : 파리채의 크기가 전체 배열을 나가지 않게 하기 위함
        for j_array in range(N-(M-1)):                          
            array[i_array][j_array] # 0 0                       # 배열 전체를 둘러보는 반복문
            result.append(sum_)                                 # sum 값을 result에 append
            sum_ = 0                                            # sum 값을 0으로 초기화
            for i in range(M):                                  # 파리채의 범위
                for j in range(M):
                    sum_ += array[i_array + i][j_array + j]     # array[배열 기준 + i(파리채의 크기)]를 구해준다
    
    result.remove(0)                                         
    
    '''
    23번 줄 설명 : (13번에 먼저 들어간 0을 지워준다) 없어도 문제 pass에는 상관이 없었습니다
    값을 더해서 list로 만드는 방법밖에 떠오르지 않았지만 배운 것들을 생각하면
    저는 더 좋은 방법을 분명 알고 있다고 생각합니다.. 하지만 그게 떠오르지 않아요 ㅠㅠ
    '''
    
    max_result = max(result)                                    # max 값을 할당해준다.      

    # 출력문 

    print(f'#{tc} {max_result}')                    






