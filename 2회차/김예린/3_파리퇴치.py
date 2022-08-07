import sys

t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())        # n == 배열, m == 파리채 면적 

    metrix = []
    for _ in range(n):                      # 배열 만들기
        metrix.append(list(input().split()))

    max_flies = 0
    
    for i in range(n):
        for j in range(n):
            
            hit = 0
            for x in range(j, j + m): 
                if x > n -1:
                    break
                for y in range(i + i +m):
                    if y > n -1: 
                        break
                    hit += int(metrix[x][y])
                            
            if max_flies < hit:
                max_flies = hit
    
    print('#{} {}'.format(test_case, max_flies))

sys.stdin = open("_파리퇴치.txt")
