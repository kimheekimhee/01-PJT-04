import sys
from pprint import pprint

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())

    fly_list = []
    for _ in range(N):
        data = list(map(int, input().split()))
        fly_list.append(data) # 여기까지 파리갯수 리스트 만들기 
    
    a = 0 # a,b를 range(시작위치, 끝나는 위치)랑 연동을 시켜  
    b = 0 # 해당 구역의 최대값을 찾아내는 방식으로 구현하였습니다.
    sum_list = []
    while True:
        sum_ = 0
        for i in range(b,M+b):
            for j in range(a, M+a):
                sum_ += fly_list[i][j]
                sum_list.append(sum_)
        a += 1 # 첫 구연 계산이 되면 a를 우선 증가(오른쪽으로 이동)
        if a + M == N+1: # 그러다 벽을 만나면 
            a = 0 # a는 초기화 
            b += 1 # b를 증가시켜 한칸 아래로 내려가 계산시작
            if b + M == N + 1: # 아래 벽을 만나면 계산 중지 
                break
    print(f"#{t} {max(sum_list)}") # 그중 최대값. 
    # 만약 위치가지 알아야 했다면 
    # 딕셔너리를 사용하여 a,b를 키를 만들어 값을 저장후 해당값에 해당하는 키를 찾고 a,b값을 알아내고
    # 그 값을 토대로 위치를 출력했을거 같습니다. 
"""
나는 이중 구문 사용 
쌤은 4중 구문을 통해 범위 문제 해결.
"""

    

