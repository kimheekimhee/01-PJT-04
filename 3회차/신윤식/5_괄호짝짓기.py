import sys

sys.stdin = open("./3회차/신윤식/_괄호짝짓기.txt")

open = ['{', '[', '(', '<']
close = ['}', ']', ')', '>']

for _ in range(1,11):
    len_x = int(input())
    x = input()
    stack = []

    for i in x:
        if i in open:
            stack.append(i)
        elif i in close:
            if len(stack) == 0:
                continue
            elif i == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    print(f'#{_} 0')
                    break
            elif i == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    print(f'#{_} 0')
                    break
            elif i == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    print(f'#{_} 0')
                    break
            elif i == '>':
                if stack[-1] == '<':
                    stack.pop()
                else:
                    print(f'#{_} 0')
                    break
    else:
        if len(stack) == 0:
            print(f'#{_} 1')
        # elif len(stack) > 0:
        #     print(f'#{_} 0')