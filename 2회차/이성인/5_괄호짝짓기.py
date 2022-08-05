import sys

sys.stdin = open("_괄호짝짓기.txt")

for t in range(1,11): # 제가 D4을 풀다니 감격스럽네요. 그중 쉬운 문제 였던거 같지만요.ㅋㅋ
    bracket = []
    _ = input()
    data = input()
    for char in data:
        if char in ["(","[","{","<"]: # 이 넷을 만나면 리스트에 추가 
            bracket.append(char)
        else: # 아니면 각각 짝이 맞는지 확인. 
            if char == ")":
                a = bracket.pop()
                if a != "(":
                    print(f"#{t} 0")
                    break
            elif char == "]":
                a = bracket.pop()
                if a != "[":
                    print(f"#{t} 0")
                    break
            elif char == "}":
                a = bracket.pop()
                if a != "{":
                    print(f"#{t} 0")
                    break
            elif char == ">":
                a = bracket.pop()
                if a != "<":
                    print(f"#{t} 0")
                    break
    else:   
        print(f"#{t} 1")

# pop pop() 은 다른거구나.