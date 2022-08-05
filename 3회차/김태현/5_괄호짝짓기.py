import sys
sys.stdin = open("_괄호짝짓기.txt")

for i in range(1, 11):
    bracket_num = int(input())
    bracket_list = input()

    left_bracket = []

    left = "([{<"

    dic = {
        "(" : ")",
        "[" : "]",
        "{" : "}",
        "<" : ">"
    }

    isBool = True
    
    for bracket in bracket_list:
        # 왼쪽 괄호 나오면
        if bracket in left:
            left_bracket.append(bracket)
        
        # 오른쪽 괄호 나오면
        else:
            if left_bracket:

                if dic[left_bracket[-1]] == bracket:
                    left_bracket.pop()
                else:
                    isBool = False
                    break

    # print(len(left_bracket), "len(left)")

    if len(left_bracket):
        isBool = False
    else:
        isBool = True

    if isBool:
        print(f"#{i} 1")
    else:
        print(f"#{i} 0")