import sys

sys.stdin = open("_괄호짝짓기.txt")

def 괄호(a):
    if a == '(': return ')' 
    elif a == ')': return '('
    elif a =='[': return ']'
    elif a ==']': return '['
    elif a == '{': return '}'
    elif a == '}': return '{'
    elif a == '<': return '>'
    elif a == '>': return '<'                          

for c in range(1,11):
    T = int(input())
    lst = list((input()))
    #lst[len(lst)-1]    
    tmp = []
    while(lst):
        if not tmp:
            tmp.append(lst.pop())
         
        if 괄호(lst[len(lst)-1]) in tmp:
            tmp.remove(괄호(lst.pop()))
             
        else:
            tmp.append(lst.pop())
    
    if not tmp:
        print(f'#{c} 1')
    else:
        print(f'#{c} 0')
            
       
    
    
    
    
    
    
     
   
        