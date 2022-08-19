import sys

sys.stdin = open("_괄호짝짓기.txt")

# 주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
# 예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 
# 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
 

for i in range(10):
    N = int(input())
    lst_ = list(input())
    check_ = list()
    answer = 1
    for bracket in range(N):
        if lst_[bracket] == ")":
            if '(' in check_:
                check_.pop(check_.index("("))
            else:
                answer = 0
                break
        if lst_[bracket] == ">":
            if '<' in check_:
                check_.pop(check_.index("<"))
            else:
                answer = 0
                break
        if lst_[bracket] == "}":
            if '{' in check_:
                check_.pop(check_.index("{"))
            else: 
                answer = 0
                break
        if lst_[bracket] == "]":
            if '[' in check_:
                check_.pop(check_.index("["))
            else:
                answer = 0
                break
        else:
            check_.append(lst_[bracket])

    print("#{} {}".format(i+1, answer))