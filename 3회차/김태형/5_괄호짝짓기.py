# import sys

# sys.stdin = open("_괄호짝짓기.txt")

for i in range(1,11):
    n = int(input())
    s = input()
    if s.count('(')==s.count(')') and s.count('[')==s.count(']') and s.count('{') == s.count('}') and s.count('<') == s.count('>'):
        print("#%d %d" %(i, 1))
    else:
        print("#%d %d" %(i, 0))