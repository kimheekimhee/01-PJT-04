import sys

sys.stdin = open("_괄호짝짓기.txt")
'''
접근방법
 
문자열 replace로 괄호들을 없애면서 짝이 맞다면 길이가 0 이 됨 

'''
tc = 10

for tc in range(10):

    n = int(input())
    str_ = input()
    for i in range(n):
    
        if '()' in str_:
            str_ = str_.replace('()','')
        if '[]' in str_:
            str_ = str_.replace('[]','')
        if '<>' in str_:
            str_ = str_.replace('<>' ,'')
        if '{}'in str_:
            str_ = str_.replace('{}','')

    if len(str_) == 0:
        print(f'#{tc+1}',1)

    else:
        print(f'#{tc+1}',0)