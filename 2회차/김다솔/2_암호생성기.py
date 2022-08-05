import sys

sys.stdin = open("_암호생성기.txt")

# T = int(input()) 음서,, 
T = 10
for _ in range(1, T+1):
    tc = int(input())
    pw = list(map(int, input().split()))
    # print(pw)
    
    rule = 1
    a = 1
    while pw[-1]:   
        for i in range(1, 6):
            pw.append(pw.pop(0)-i)
            
            if pw[-1] <= 0:
                pw[-1] = 0
                            
                break
    print(f'#{tc}', *pw)       
        