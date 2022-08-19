t = int(input())

# m x m 의 합이 가장 큰 부분을 때리면 된다

for tc in range(1, t+1):
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]
   
    n = M-1
    max_v = 0
    #N-M+1 범위의 idx만큼 순회
    for i in range(N-n):
        for j in range(N-n):
            sum_v = 0
            #해당 인덱스에서 MxM 범위 내 원소합을 저장
            for di in range(M):
                for dj in range(M):
                    sum_v += table[i+di][j+dj]
            #최대값과 비교하며 최대값 저장
            if sum_v > max_v:
                max_v = sum_v
    
    print('#{} {}'.format(tc, max_v))