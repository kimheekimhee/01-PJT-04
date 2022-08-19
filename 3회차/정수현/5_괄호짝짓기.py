import sys

sys.stdin = open("_괄호짝짓기.txt")

bracket_match = {
    '{':'}', 
    '[':']',
    '(':')',
    '<':'>'
    }

def bracket_mating(s):
    brackets= []
    for i in s:
        if i in ['{', '[', '<', '(']:
            brackets.append(i)
        elif i in ['}', ']', '>', ')']:
            if not brackets or bracket_match[brackets.pop()] != i:
                return 0
    if brackets:
        return 0
    else:
        return 1



for t in range(1, 11):
    input()
    print(f'#{t}',bracket_mating(input()))
