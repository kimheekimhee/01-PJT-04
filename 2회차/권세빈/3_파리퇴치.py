import sys
from pprint import pprint
sys.stdin = open("_파리퇴치.txt")

T = int(input())
for t in range(1, T+1):
    n, m = map(int,input().split())
    fly = [list(map(int,input().split())) for _ in range(n)]
    fly_che = []
    
    # 파리채가 움직이는 범위 지정
    for k in range(n-m+1): 
        for l in range(n-m+1): 
            # 파리 죽인 수
            kill = 0
            # 파리채 범위
            for i in range(m):
                for j in range(m):
                    # 범위 안에서 움직이면서 파리 죽인 수 모으기 
                    kill += fly[i+k][j+l]
            # 리스트에 추가        
            fly_che.append(kill)
    # 리스트 안에서 최대값 출력
    print(f'#{t}',max(fly_che))