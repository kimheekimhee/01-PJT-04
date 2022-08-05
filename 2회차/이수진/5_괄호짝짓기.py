import sys

sys.stdin = open("_괄호짝짓기.txt")

for t in range(10):
    n=int(input())
    string=input()
    stack = []
    flag = True
    for i in range(n):
        if string[i] in '{[(<':
            stack.append(string[i])
        elif string[i] in '}])>':
            if stack:
                pop = stack.pop()
                if (pop == '(' and string[i] == ')') or (pop == '[' and string[i] == ']') or (pop == '{' and string[i] == '}') or (pop == '<' and string[i] == '>'):
                    flag = True
                else:
                    flag = False
                    break
            else:
                flag = False
                break
    print(f'#{t+1} {1 if flag else 0}')