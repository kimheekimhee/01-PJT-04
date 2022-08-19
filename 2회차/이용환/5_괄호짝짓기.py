import sys

sys.stdin = open("_괄호짝짓기.txt")
T = 10
for i in range(1, T+1):
    cast = int(input())
    bracket = input()
    result = []
    open = ['<', '(', '{', '[']
    close = ['>', ')', '}', ']']
    cnt = 1
    for j in bracket:
        if j in open:
            result.append(j)
        else:
            if open.index(result[-1]) == close.index(j):
                result.pop()
            else:
                cnt = 0
                break
    print(f'#{i}', cnt)