import sys

sys.stdin = open("_괄호짝짓기.txt")
t = 10
for i in range(t):
    length = int(input())
    arr = list(input())
    dic = {')':'(', ']':'[', '>':'<', '}':'{'} # 스택에서 빼낼 때, 비교를 위해서 역순으로 key, value 
    stk = []
    for j in arr:
        if j in dic.values(): # 시작하는 괄호면 스택에 추가
            stk.append(j)
        if j in dic.keys():
            if len(stk) < 1: # 스택에 아무것도 없을 때, 닫히는 괄호가 오면 유효하지 않은 문자열
                break
            if stk[-1] == dic[j]: # 스택의 마지막 요소(stk[-1])가 짝(> ,<)이 아니면 유효하지 않은 문자열
                stk.pop()
            else:
                break
    print(f'#{i + 1}', end=' ')
    if len(stk) > 1:
        print(0)
    else:
        print(1)

