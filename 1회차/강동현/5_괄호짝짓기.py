import sys

sys.stdin = open("_괄호짝짓기.txt")

for z in range(10):
    a = int(input())
    line = input()
    stack = []
    lft = ['(','{','[','<']
    rgt = [')','}',']','>']
    for i in range(a):
        scnt = 0
        if line[i] in lft:
            stack.append(line[i])
        elif line[i] in rgt:
            if lft.index(stack[-1]) ==rgt.index(line[i]):
                stack.pop()
            else:
                break
    if len(stack) !=0:
        print(f'#{z+1} 0')
    else:
        print(f'#{z+1} 1')