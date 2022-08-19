import sys

sys.stdin = open("_괄호짝짓기.txt")

for _ in range(10): #10개의 테스트케이스
    
    K = int(input())
    bracket = list(input())
    # print(K)
    # print(bracket)

    sub = [] #임시창소 제작 stak
    for brak in bracket: #for a in range(K): -> 숫자를 받아서 인덱스를 활용하느냐 /문자인 괄호를 직접 받아서 활용하느냐
        if brak == '(' or brak == '[' or brak == '{' or brak == '<': #좌측괄호는 무조건 임시창고에 넣음
            sub.append(brak)
        else:
            if len(sub) <= 0 : #임시저장소에 넣어둔게 있는가
                sub.append(brak)
                break
            else : #임시창고에 무언가가 있음
                check = sub.pop()
                if check == '(' and brak ==')': #임시창고에서 꺼낸 것과 리스트에 있는 괄호는 비교한다
                    continue
                elif check == '<' and brak =='>':
                    continue
                elif check == '[' and brak ==']':
                    continue
                elif check == '{' and brak =='}':
                    continue
                else:
                    #print(0)
                    break

    if len(sub) == 0: 
        print(f'#{_+1}',1)
    else:
        print(f'#{_+1}',0)
    #창고가 비었지만 작동안하는 경우가 있지않을까??
    #case1 - 우측괄호가 나왔는데. 임시창고가 비여있다면 1이 출력되네 -> if len(sub) <= 0 경우 sub창고에 이물질을 넣고 브레이크