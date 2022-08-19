import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    # print(flies)
    killed = [] 
    # max(sum([i][j], [i+1][j], [i][j+1], [i+1][j+1])) -> m 2일때만해당,, 
    # i +- 1~m, j +- 1~m 이거 생각해서 반복범위정하기 
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            # for m in range(M): # 이 반복을 어케하지.................. 
            #     cnt += flies[i+m][j] + flies[i][j+m] + flies[i+m][j+m]
            for im in range(M):
                for jm in range(M):
                    cnt += flies[i+im][j+jm]
                killed.append(cnt)
    print(f'#{tc}', max(killed))