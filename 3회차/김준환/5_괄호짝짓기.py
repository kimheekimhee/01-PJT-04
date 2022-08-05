# import sys

# sys.stdin = open("_괄호짝짓기.txt")

t = 10
for test in range(t):
    long = int(input())
    gual = input()
    small_g, middle_g, big_g, angle_g = 0, 0, 0, 0
    result = 1
    for text in gual:
        if text == '(':
            small_g += 1
        elif text == '[':
            middle_g += 1
        elif text == '{':
            big_g += 1
        elif text == '<':
            angle_g += 1
        elif text == ')':
            small_g -= 1
        elif text == ']':
            middle_g -= 1
        elif text == '}':
            big_g -= 1
        elif text == '>':
            angle_g -= 1
        if small_g < 0 or middle_g < 0 or big_g < 0 or angle_g < 0:
            result = 0
            break
    if small_g != 0 or middle_g != 0 or big_g != 0 or angle_g != 0:
        result = 0
    print(f'#{test+1} {result}')