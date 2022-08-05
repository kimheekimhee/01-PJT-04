import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())
for z in range(T):
    a, b = map(int, input().split())
    result = 0
    board = []
    for y in range(a):
        line = list(map(int, input().split()))
        board.append(line)
    ans = 0
    for x in range(a):
        cnt = 0
        for w in range(a):
            if (board[x][w] == 1):
                cnt+=1
                if cnt == b+1:
                    ans-=1
                elif cnt == b :
                    ans+=1
            else:
                cnt = 0
        cnt1 = ans
    ans = 0
    for x in range(a):
        cnt = 0
        for w in range(a):
            if (board[w][x] == 1):
                cnt+=1
                if cnt == b+1:
                    ans-=1
                elif cnt == b :
                    ans += 1
            else:
                cnt = 0
        cnt2 = ans
    tcnt = cnt1+cnt2
    print(f'#{z+1} {tcnt}')