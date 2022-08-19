import sys

sys.stdin = open("_암호생성기.txt")

Tc = 10
for ii in range(Tc):
    T = int(input())
    case = list(map(int,input().split()))
    cnt = 0
    while 1:
        for i in range(1,6):
            case.append(case[0]-i)
            case.remove(case[0])
            if case[7] <= 0:
                break
        if case[7] <= 0:
                break
    case[7] = 0
    case = list(map(str,case))
    print(f"#{ii+1} {' '.join(case)}")