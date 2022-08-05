import sys

sys.stdin = open("_괄호짝짓기.txt")


T = 10

for i in range(T):
    word_len = int(input())
    word = input()
    
    word_stack = []
    
    for w in word:
        word_stack.append(w)
        if w == ')' and '(' in word_stack:
            word_stack.pop()
            word_stack.remove('(')
        if w == ']' and '[' in word_stack:
            word_stack.pop()
            word_stack.remove('[')
        if w == '>' and '<' in word_stack:
            word_stack.pop()
            word_stack.remove('<')
        if w == '}' and '{' in word_stack:
            word_stack.pop()
            word_stack.remove('{')
            
    if len(word_stack):
        print(f'#{i+1}', '0')
    else:
        print(f'#{i+1}', '1')
    