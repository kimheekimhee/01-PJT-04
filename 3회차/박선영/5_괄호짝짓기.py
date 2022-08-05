import sys

sys.stdin = open("_괄호짝짓기.txt")
# 노가다 방법 1
for test_case in range(1, 11):
    n = int(input())
    parenth = input()
    a = []
    b = []
    c = []
    d = []
    ans = 0
    for p in parenth:
        if p == '(':
            a.append(p)
        elif p == ')':
            if len(a) > 0:
                a.pop()
            else:
                ans = 0
                break

        elif p == '[':
            b.append(p)
        elif p == ']':
            if len(b) > 0:
                b.pop()
            else:
                ans = 0
                break

        elif p == '{':
            c.append(p)
        elif p == '}':
            if len(c) > 0:
                c.pop()
            else:
                ans = 0
                break
        elif p == '<':
            d.append(p)
        else:
            if len(d) > 0:
                d.pop()
            else:
                ans = 0
                break
    if len(a) + len(b) + len(c) + len(d) == 0:
        ans = 1
    print(f'#{test_case} {ans}')
