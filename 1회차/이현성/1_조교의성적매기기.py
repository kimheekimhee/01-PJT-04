a = int(input())

for t in range(1, a+1):
    b, c = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(b)]
    sum_ = 0
    
    for i in range(b):
        cnt = 0
        for j in range(b):
            if matrix[i][j] == 1:
                cnt += 1
                if cnt == c:
                    sum_ += 1
            else:
                cnt = 0
        if cnt == c:
            sum_ += 1
        
    
    for i in range(b):
        cnt = 0
        for j in range(b):
            if matrix[j][i] == 1:
                cnt += 1
                if cnt == c:
                    sum_ += 1
            else:
                cnt = 0        
        if cnt == c:
            sum_ += 1
                
    print(f'#{t} {sum_}')
        