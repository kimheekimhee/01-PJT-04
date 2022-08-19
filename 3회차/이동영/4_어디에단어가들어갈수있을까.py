import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
'''
접근방법
 
행과 열을 cnt에 누적하면서 길이가 맞고 딱 들어맞는지 확인

'''
tc = int(input())

for tc in range(tc):

    n, m = map(int, input().split())

    a = [list(map(int, input().split())) for _ in range(n)]
    
    result = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[i][j] == 1:
                cnt += 1
            if a[i][j] == 0 or j == n-1:
                if cnt == m:
                    result += 1
                cnt = 0 
                   
    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[j][i] == 1:
                cnt += 1
            if a[j][i] == 0 or j == n-1:
                if cnt == m:
                    result += 1
                cnt = 0
                        
                            
    print(f'#{tc+1}', result)