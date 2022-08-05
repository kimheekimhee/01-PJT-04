import sys

sys.stdin = open("_괄호짝짓기.txt")

open_b = ['(', '[', '{', '<']
close_b = [')', ']', '}', '>']

for i in range(1, 11):
    len_ = int(input())
    bracket = list(input())                                 # 확인할 괄호들을 입력받은 리스트

    stack_ = []
    check = True                                            # 결과를 저장하기 위한 boolean

    for j in bracket:                                       # 괄호들의 리스트에서
        if j in open_b:                                     # 하나의 괄호가 여는 괄호라면
            stack_.append(j)                                # 스택에 저장한다
        elif j in close_b:                                  # 닫는 괄호라면
            # 닫는 괄호가 몇 번째 인덱스의 괄호인지 확인한다
            # 확인한 인덱스의 여는 괄호를 불러와 스택에서 pop한 값과 같은지 확인한다
            if stack_.pop() != open_b[close_b.index(j)]:
                # 스택에 저장된 값이 확인하고자 하는 닫는 괄호와 짝이 아니면 결과를 False로 변경하고 종료
                check = False
                break

    if check == True:
        print(f'#{i} 1')                                    # 결과가 True면 1 출력
    else:
        print(f'#{i} 0')                                    # 결과가 False면 0 출력
