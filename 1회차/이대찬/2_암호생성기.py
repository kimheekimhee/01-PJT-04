import sys

sys.stdin = open("_암호생성기.txt")

for c in range(0,10):
    T = int(input())
    tmp = 0
    lst = list(map(int,input().split()))
    while(lst[len(lst)-1] > 0):
        for i in range(1,6):
            tmp = lst.pop(0) 
            lst.append(tmp-i)
            if lst[len(lst)-1] <=0:
                break
            
    if lst[len(lst)-1] <0:
        lst[len(lst)-1] = 0

    print(f'#{T}',end=' ') 
    for n in lst:
        print(f'{n}',end=' ')
    print()
 
        
        

 
       
    # print(f'#{t} {result[K]}')
            