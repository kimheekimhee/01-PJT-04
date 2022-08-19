t = int(input())
 
for tc in range(1, t+1) :
    n, k = map(int, input().split()) # n = 퍼즐의 크기 k = 글자의 길이
    table = [list(map(int, input().split())) for _ in range(n)]
 
    result = 0
    # 가로 확인
    for i in range(n) :
        cnt = 0
        for j in range(n) :
            if table[i][j] == 1 : #빈칸 개수 세기
                cnt += 1
            if table[i][j] == 0 or j == n -1 : # 넣을 수 있는 칸의 개수
                if cnt == k :
                    result += 1
                if table[i][j] == 0 : # 검은 칸 나오면 초기화
                    cnt = 0 
 
    # 세로 확인
    for i in range(n) :
        cnt = 0
        for j in range(n) :
            if table[j][i] == 1 :
                cnt += 1
            if table[j][i] == 0 or j == n - 1 :
                if cnt == k :
                    result += 1
                if table[j][i] == 0 :
                    cnt = 0
 
    print('#%d %d' % (tc, result)) 