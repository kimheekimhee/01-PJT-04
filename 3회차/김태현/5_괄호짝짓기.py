import sys
sys.stdin = open("_괄호짝짓기.txt")

import heapq as hq

for i in range(1, 11):
    bracket_list = input()
    print("=============================")

    round_bracket = [] # ( )
    square_bracket = [] # [ ]
    curly_bracket = [] # { }
    angle_bracket = [] # < >

    left = "([{<"
    right = ")]}>"

    
    for bracket in bracket_list:
        # 둥근 괄호 ()
        if bracket == "(":
            hq.heappush(round_bracket, bracket)
        elif bracket == ")":
            if len(round_bracket) != 0:
                hq.heappop(round_bracket)
            hq.heappush(round_bracket, bracket)

        # 네모 괄호 []
        if bracket == "[":
            hq.heappush(square_bracket, bracket)
        elif bracket == "]":
            if len(square_bracket) != 0:
                hq.heappop(square_bracket)
            hq.heappush(square_bracket, bracket)

        # 브로콜리 괄호 {}
        if bracket == "{":
            hq.heappush(curly_bracket, bracket)
        elif bracket == "}":
            if len(curly_bracket) != 0:
                hq.heappop(curly_bracket)
            hq.heappush(curly_bracket, bracket)

        # 꺾인 괄호 <>
        if bracket == "<":
            hq.heappush(angle_bracket, bracket)
        elif bracket == ">":
            if len(angle_bracket) != 0:
                hq.heappop(angle_bracket)
            hq.heappush(angle_bracket, bracket)
    

    print(*round_bracket)
    print(*square_bracket)
    print(*curly_bracket)
    print(*angle_bracket)

    if len(round_bracket) + len(square_bracket) + len(curly_bracket) + len(angle_bracket) == 0:
        result = 1
    else:
        result = 0

    print(f"#{i} {result}")