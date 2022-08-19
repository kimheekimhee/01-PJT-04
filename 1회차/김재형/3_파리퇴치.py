import sys

sys.stdin = open("_파리퇴치.txt")

# 테스트 케이스
T = int(input())

for t in range(T) :
    n, m = map(int, input().split())
    area = []
    for _ in range(n):
        area.append(list(map(int, input().split())))

    result = 0
    for i in range(n-m+1) : # 파리채가 움직을 수 있는
        for j in range(n-m+1) :
            sum_ = 0
            for x in range(m) : # 파리채 크기
                for y in range(m) : 
                    sum_ += area[i+x][j+y]
            if sum_ > result :
                result = sum_

    print(f'#{t+1} {result}')