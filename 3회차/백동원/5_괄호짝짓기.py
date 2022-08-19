import sys

sys.stdin = open("_괄호짝짓기.txt")
for a in range(1, 11):
    word_amnt = int(input())
    word = list(input())
    hamsu = []
    for b in range(word_amnt):
        popword = word.pop()
        hamsu.append(popword)
        if popword == '(':
            if ')' in hamsu:
                hamsu.remove(')')
                hamsu.remove('(')
        elif popword == '[':
            if ']' in hamsu:
                hamsu.remove('[')
                hamsu.remove(']')    
        elif popword == '{':
            if '}' in hamsu:
                hamsu.remove('{')
                hamsu.remove('}')    
        elif popword == '<':
            if '>' in hamsu:
                hamsu.remove('<')
                hamsu.remove('>')
    if len(hamsu) > 0:
        print(f'#{a} 0')
    else:
        print(f'#{a} 1')
