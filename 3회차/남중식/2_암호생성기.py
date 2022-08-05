import sys

sys.stdin = open("_암호생성기.txt")

from collections import deque

def swea_pw_gen():

    for i in range(10):
        case = int(input())
        pw_list = list(map(int, input().split()))
        pw_queue = deque(pw_list)
        
        while_checker = True
        
        while while_checker == True:
            for j in range(1,6):
                pw_queue[0] = pw_queue[0] - j
                pw_queue.rotate(-1)
                
                if pw_queue[-1] <= 0:
                    pw_queue[-1] = 0
                    print(f'#{case}',*pw_queue)
                    while_checker = False
                    break
                
swea_pw_gen()
            
    
            
        
        