from importlib import import_module
import sys

sys.stdin = open("_괄호짝짓기.txt")

for case in range(10):
    number = int(input())
    s = input()
    stack = []
    temp = True
    for i in s:
        if i == '(' or i == '[' or i == '{' or i == '<':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i == '}':
            if len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            else:
                stack.append('}')
                break
        elif i == '>':
            if len(stack) != 0 and stack[-1] == '<':
                stack.pop()
            else:
                stack.append('>')
                break

    if len(stack) == 0:
        print(f'#{case+1} {1}')
    else:
        print(f'#{case+1} {0}')