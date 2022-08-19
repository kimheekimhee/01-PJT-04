import sys

sys.stdin = open("_괄호짝짓기.txt")

for t in range(1, 11):
    a = input()
    gh = input()
    check_1 = []
    check_2 = []
    check_3 = []
    check_4 = []
    sign = 1
    for g in gh:
        if g == '(':
            check_1.append('(')
        elif g == ')':
            if len(check_1) > 0:
                check_1.pop()
            else:
                sign = 0
                break
        elif g == '[':
            check_2.append('[')
        elif g == ']':
            if len(check_2) > 0:
                check_2.pop()
            else:
                sign = 0
                break
        elif g == '{':
            check_3.append('{')
        elif g == '}':
            if len(check_3) > 0:
                check_3.pop()
            else:
                sign = 0
                break
        elif g == '<':
            check_4.append('<')
        elif g == '>':
            if len(check_4) > 0:
                check_4.pop()
            else:
                sign = 0
                break
    print(f'#{t} {sign}')