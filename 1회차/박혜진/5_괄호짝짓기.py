import sys

sys.stdin = open("_괄호짝짓기.txt")

for num in range(1, 11) :
    gualho_len = int(input())
    gualho = input()

    g = []
    for _ in range(gualho_len) :
        for i in gualho :
            if i == '(' :
                g.append(i)
            elif i == ')' :
                if '(' in g :
                    g.remove('(')
                else :
                    g.append(i)

            if i == '[' :
                g.append(i)
            elif i == ']' :
                if '[' in g :
                    g.remove('[')
                else :
                    g.append(i)

            if i == '{' :
                g.append(i)
            elif i == '}' :
                if '{' in g :
                    g.remove('{')
                else :
                    g.append(i)

            if i == '<' :
                g.append(i)
            elif i == '>' :
                if '<' in g :
                    g.remove('<')
                else :
                    g.append(i)

    if g == [] :
        print(f'#{num} {1}')

    else :
        print(f'#{num} {0}')
            
