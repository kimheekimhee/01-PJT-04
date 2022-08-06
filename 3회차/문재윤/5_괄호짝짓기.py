import sys

sys.stdin = open("_괄호짝짓기.txt")


for i in range(1,11):
    n = int(input())
    garo = input()
    co = True
    li = []
    for j in garo:
        if '(' == j:
            li.append('(')
         
        elif ")" == j:
            if '(' in li:
              li.remove('(')
          
            elif '(' not in li:
                co = False
                break
        if '[' == j:
            li.append('[')
            
        elif "]" == j:
            if '[' in li:
              li.remove('[')
             
            elif '[' not in li:
                co = False
                break
        if '<' == j:
            li.append('<')
           
        elif ">" == j:
            if '<' in li:
              li.remove('<')
             
            elif '<' not in li:
                co = False
                break
        if '{' == j:
            li.append('{')
            
        elif "}" == j:
            if '{' in li:
              li.remove('{')
             
            elif '{' not in li:
                co = False
                break

    print(li)
    if co == True and len(li) == 0:
        print(f'#{i} 1')   
    else:
        print(f'#{i} 0')