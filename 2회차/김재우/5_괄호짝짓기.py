import sys

sys.stdin = open("_괄호짝짓기.txt")



for tc in range(1, 11):
    word = int(input())
    word_list = (input())


    check1 = 0              # '()' 체크해 줄 변수
    check2 = 0              # '[]' 체크해 줄 변수
    check3 = 0              # '{}' 체크해 줄 변수
    check4 = 0              # '<>' 체크해 줄 변수
    
    for i in word_list:     # word_list 한 바퀴 돌아돌아
        
        if i == '(':        # ( 가 등장하면
            check1 += 1     # check1에 +=1 
        if i == ')':        
            check1 -= 1     # -=

        if i == '[':        # 위와 같음.
            check2 += 1 
        if i == ']':
            check2 -= 1   
        
        if i == '{':        # ...
            check3 += 1 
        if i == '}':
            check3 -= 1

        if i == '<':        # ...
            check4 += 1 
        if i == '>':
            check4 -= 1 
    
    if check1 == 0 and check2 == 0 and check3 == 0  and check4 == 0:        # if 모든 변수가 0이라면
        print(f'#{tc} 1')                                                   # 유효하다는 1 출력
    else:
        print(f'#{tc} 0')                                                   # 아니면 유효하지 않다는 0 출력