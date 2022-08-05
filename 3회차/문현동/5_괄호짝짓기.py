import sys

sys.stdin = open("_괄호짝짓기.txt")

for test_case in range(1, 11):
    s_len = int(input()) # 문자열의 길이
    chaos = input() # 어지러운 문자열
    
    for _ in range(s_len):
        ref = True # 참조값은 True로 시작
        ps = [] # 하나씩 검사할 스택
        
        for s in chaos:
            if ref:
                if s == '(': # 여는 괄호가 나오면 ps 에 추가
                    ps.append(s)
                elif s == ')': # 닫히는 괄호가 나왔을 때,
                    if ps[-1] == '(': # 스택의 마지막이 그것과 같은 여는 괄호여야 한다.
                        ps.pop()
                    else:
                        ref = False # 아닌 경우 참조값은 거짓이 되고 반복문 종료.
                        break
                    
                elif s == '[':
                    ps.append(s)
                elif s == ']':
                    if ps[-1] == '[':
                        ps.pop()
                    else:
                        ref = False
                        break
                    
                elif s == '{':
                    ps.append(s)
                elif s == '}':
                    if ps[-1] == '{':
                        ps.pop()
                    else:
                        ref = False
                        break
                    
                elif s == '<':
                    ps.append(s)
                elif s == '>':
                    if ps[-1] == '<':
                        ps.pop()
                    else:
                        ref = False
                        break
                else:
                    continue
                
    print(f"#{test_case} {int(ref)}")