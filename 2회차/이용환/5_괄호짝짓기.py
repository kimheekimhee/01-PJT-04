import sys

sys.stdin = open("_괄호짝짓기.txt")
T = 10
for i in range(1, T+1):
    cast = int(input())
    bracket = input()
    result = []
    for j in bracket:
        if j in '(<[{':
            result.append(j)
        elif j == ')':
            if result[-1] == '(':
                result.pop()
            else:
                print(f'#{i}', 0)
                break
        elif j == '>':
            if result[-1] == '<':
                result.pop()
            else:
                print(f'#{i}', 0)
                break
        elif j == '}':
            if result[-1] == '{':
                result.pop()
            else:
                print(f'#{i}', 0)
                break      
        elif j == ']':
            if result[-1] == '[':
                result.pop()
            else:
                print(f'#{i}', 0)
                break
    if len(result) == 0:
        print(f'#{i}', 1)
     