import sys

sys.stdin = open("_괄호짝짓기.txt")



for tc in range(1, 11):
    word = int(input())
    word_list = (input())


    check1 = 0
    check2 = 0
    check3 = 0
    check4 = 0 
    
    for i in word_list:
        
        if i == '(':
            check1 += 1
        if i == ')':
            check1 -= 1

        if i == '[':
            check2 += 1 
        if i == ']':
            check2 -= 1   
        
        if i == '{':
            check3 += 1 
        if i == '}':
            check3 -= 1

        if i == '<':
            check4 += 1 
        if i == '>':
            check4 -= 1 
    
    if check1 == 0 and check2 == 0 and check3 == 0  and check4 == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')