import sys

sys.stdin = open("_파리퇴치.txt")
'''
접근방법
 
입력받은 M 값들을 cnt 에 누적해서 더한다음 리스트에 담아 가장 큰값을 출력

'''
tc = int(input())

for tc in range(tc):
    n, m = map(int,input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    
    list_= []
    cnt = 0
    for i in range(n):
        for j in range(n):
            
            if i > n - m or j > n - m :
                continue
            else:
                for k in range(i,i+m):
                    for p in range(j,j+m):
                        cnt += a[k][p] 
                list_.append(cnt)
                cnt = 0
    print(f'#{tc+1}', max(list_))