from ast import expr_context


num = int(input())
strlist = list(input())
i =0
while True:
    try:
        temp = strlist[i]
        if temp == '(':
            strlist.remove('(')
            strlist.remove(')')
        elif temp == '{':
            strlist.remove('{')
            strlist.remove('}')
        elif temp == '[':
            strlist.remove('[')
            strlist.remove(']')
        elif temp == '<':
            strlist.remove('<')
            strlist.remove('>')
        i += 1
        if i == len(strlist)-1:
            print(f'i는 {i}')
            print(f'strlist의 길이는 {len(strlist)}')
            i = 0
    except ValueError as e:
        print(strlist)
        print(e)
        break