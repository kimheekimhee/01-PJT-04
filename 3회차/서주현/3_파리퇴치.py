import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for t in range(1, T+1) :
    n, m = list(map(int, input().split()))

    pari = [list(map(int, input().split())) for i in range(n)]
    result = 0
    for i in range(n-m+1) :
        for j in range(n-m+1) :
            num = 0
            for a in range(m) :          ## 위의 range(n-m+1)과 range(m)의 합이 n으로 된다.
                for b in range(m) :
                    next_pari = pari[a+i][b+j]
                    num += next_pari
            # num = pari[i][j] + pari[i+1][j] + pari[i][j+1] + pari[i+1][j+1] ## 이건 2x2일때. 
            if num > result :
                result = num
                

    print(f'#{t} {result}')

