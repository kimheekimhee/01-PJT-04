import sys

sys.stdin = open("_암호생성기.txt")

for test_case in range(10):
    T = int(input())
    p = [*map(int, input().split())]
    
    while 1:
        if p[-1] <= 0:
            p[-1] = 0
            break
        else:
            for i in range(1, 6):
                if p[-1] <= 0:
                    p[-1] = 0
                    break
                else:
                    p.append(p.pop(0) - i)
    
    p = map(str, p)
    
    print(f"#{T} {' '.join(p)}")