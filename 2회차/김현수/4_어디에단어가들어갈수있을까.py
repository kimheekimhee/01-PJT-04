import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
from pprint import pprint

T = int(input())

for _ in range(T):
    N, K = map(int,input().split()) 
    NN = [list(map(int,input().split())) for i in range(N) ] 
    # print(N, K)
    # pprint(NN)

    cnt = 0 #단어가 들어갈수 있는지 카운팅 
    cnt_sum = 0 #단어가 들어갈수 있는곳 합계
    for a in range(N):
        for b in range(N): #NN배열 둘러보기
            if NN[a][b]  == 1:  
                cnt += 1                        
            elif NN[a][b] == 0:
                if cnt == K :
                    cnt_sum += 1
                cnt = 0  #들여쓰기를 주의하자 
            if  b == N-1 :
                if cnt == K :
                    cnt_sum += 1
                cnt = 0
    
    for a in range(N):
        for b in range(N): #NN배열 둘러보기
            if NN[b][a]  == 1:  
                cnt += 1                        
            elif NN[b][a] == 0:
                if cnt == K :
                    cnt_sum += 1
                cnt = 0  #들여쓰기를 주의하자 
            if  b == N-1 :
                if cnt == K :
                    cnt_sum += 1
                cnt = 0
    
    print(f'#{_+1}',cnt_sum)