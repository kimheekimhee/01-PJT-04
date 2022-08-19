# 4 종류의 괄호문자들 '()', '[]', '{}', '<>' 로 이루어진 문자열이 주어진다.
# 이 문자열에 사용된 괄호들의 짝이 모두 맞는지 판별하는 프로그램을 작성한다.
# 예를 들어 아래와 같은 문자열은 유효하다고 판단할 수 있다.

# 이 문제는 저번에 풀었던 괄호 문제랑 유사하다.
# 종류가 4가지로 늘었을뿐!
# 그래서 배열을 이중으로 쓰고 4개로 나눠서 값을 +1 -1 받으면 될것 같다!
# 결국 전부 0이 나오지 않으면 유효하지 않은 경우인걸로!


for t in range(1, 11):
    length = int(input())
    sen = input()
    matrix = [0, 0, 0, 0]

    for s in sen:
        if s == '(':
            matrix[0] += 1
        elif s == '[':
            matrix[1] += 1
        elif s == '{':
            matrix[2] += 1
        elif s == '<':
            matrix[3] += 1

        elif s == ')':
            matrix[0] -= 1
        elif s == ']':
            matrix[1] -= 1
        elif s == '}':
            matrix[2] -= 1
        elif s == '>':
            matrix[3] -= 1
        
    res = 1
    for i in matrix:
        if i != 0:
            res = 0
            break

    # 부호와 함께 테스트 케이스의 번호를 출력하고, 
    # 공백 문자 후 유효성 여부를 1 또는 0으로 표시한다 (1 - 유효함, 0 - 유효하지 않음).
    print(f'#{t} {res}')