from multiprocessing.sharedctypes import Value
import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

for t in range(1,T+1):
    N,K = map(int,input().split())
    result = {}
    matrix = list(list(map(int,input().split())) for _ in range(N))
    for i in range(N):
        result[i+1] = (matrix[i][0]*0.35 +matrix[i][1]*0.45 + matrix[i][2]*0.2)
    result_list = list(result.values())
    result_list.sort()
    result_list.reverse()
    temp = {}
    s = int(N/10)
    g = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    r_ = 0
    g_ = 0
    while(r_<len(result_list)):
        temp[result_list[r_]] = g[g_]
        r_ +=1
        s -=1
        if s == 0:
            g_ +=1
            s = int(N/10)
    
    for dic in result:
        for tem in temp:
            if result[dic] == tem:
                result[dic] = temp[tem]
                
   
    print(f'#{t} {result[K]}')
  