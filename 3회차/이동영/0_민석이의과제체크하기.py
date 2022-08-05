import sys

sys.stdin = open("_민석이의과제체크하기.txt")

'''
 접근방법
 
 딕셔너리의 벨류를 0으로 초기화하고 제출했으면 1로 바꾼다
'''
tc = int(input())

for tc in range(tc):
    dict_ = dict()
    list_ = []
    temp = []
    
    n, m = map(int, input().split())
        
    for i in range(n):

        dict_[i+1] = 0
        
    list_ = list(map(int, input().split()))
    
    for i in list_:

        if i in dict_:
            dict_[i] = 1
          
    for i in list(dict_.keys()):
        if dict_.get(i) == 0:
            temp.append(i)
    
    print(f'#{tc+1}', end=' ')
    for i in temp:
        
        print(i, end=' ')
    print()