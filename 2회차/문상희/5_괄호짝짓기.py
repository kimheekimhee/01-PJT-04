import sys

sys.stdin = open("_괄호짝짓기.txt")

for test in range(1, 11):
    num = int(input())
    sen = list(input())

    check = []
    for i in sen:
        if i =='(' or i == '[' or i == '{' or i =='<':
            check.append(i)
        elif i ==')':
            if check[-1] != '(':
                print(f'#{test} 0')
                break
            else:
                check.pop()
        elif i == ']':
            if check[-1] != '[':
                print(f'#{test} 0')
                break
            else:
                check.pop()
        elif i == '}':
            if check[-1] != '{':
                print(f'#{test} 0')
                break
            else:
                check.pop()
        elif i == '>':
            if check[-1] != '<':
                print(f'#{test} 0')
                break
            else:
                check.pop()
    else:
        print(f'#{test} 1')

