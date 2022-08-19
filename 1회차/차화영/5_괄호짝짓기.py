import sys

sys.stdin = open("_괄호짝짓기.txt")
bracket = ['(', ')', '[',']', '{', '}', '<', '>']
for tc in range(1, 10+1):
    length = int(input())
    word = input()
    for i in word:
        for i in bracket:   
            if len('(') == len (')') and len('[') == len(']') and len('{') == len('}') and len('<') == len('>'):
                print("#{} {}".format(tc, 1))
            else:
                print("#{} {}".format(tc, 0))