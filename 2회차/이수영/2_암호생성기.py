import sys

sys.stdin = open("_암호생성기.txt")

N = int(input())
code = list(map(int, input().split()))

for j in range(1, 6):       
        code.append(code.pop(0)-int(j))
       


    

    
        
       
