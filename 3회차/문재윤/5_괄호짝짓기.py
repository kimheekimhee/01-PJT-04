import sys

sys.stdin = open("_괄호짝짓기.txt")

n = int(input())
li = []
for i in range(n):
    nn = input()
    co = True
    for ch in nn:
        if ch == '(':
            li.append('(')
        if ch == ')':
            if li:
                li.pop()
            elif not li:
                co = False
                break
        if ch == '[':
            li.append('[')
        if ch == ']':
            if li:
                li.pop()
            elif not li:
                co = False
                break
        if ch == '{':
            li.append('{')
        if ch == '}':
            if li:
                li.pop()
            elif not li:
                co = False
                break
        if ch == '<':
            li.append('<')
        if ch == '>':
            if li:
                li.pop()
            elif not li:
                co = False
                break
    if not li and co:
        print('YES')
    elif li or not co:
        print('NO')

        


    