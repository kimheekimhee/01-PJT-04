import sys

sys.stdin = open("_괄호짝짓기.txt")

for _ in range(1, 11):
    check = 0
    stack1 = []
    stack2 = []
    stack3 = []
    stack4 = []
    n = int(input())
    s = input()
    if n % 2 != 0:
        print('#', _, ' ', 0, sep='')
        continue
    for i in s:
        # ()
        if i == '(':
            stack1.append(i)
        elif i == ')':
            if len(stack1) == 0:
                print('#', _, ' ', 0, sep='')
                check = 1
                break
            stack1.pop()
        # []
        elif i == '[':
            stack2.append(i)
        elif i == ']':
            if len(stack2) == 0:
                print('#', _, ' ', 0, sep='')
                check = 1
                break
            stack2.pop()
        # {}
        elif i == '{':
            stack3.append(i)
        elif i == '}':
            if len(stack3) == 0:
                print('#', _, ' ', 0, sep='')
                check = 1
                break
            stack3.pop()
        # <>
        elif i == '<':
            stack4.append(i)
        elif i == '>':
            if len(stack4) == 0:
                print('#', _, ' ', 0, sep='')
                check = 1
                break
            stack4.pop()
    if check == 0:
        if len(stack1) == 0 and len(stack2) == 0 and len(stack3) == 0 and len(stack4) == 0:
            print('#', _, ' ', 1, sep='')
        else:
            print('#', _, ' ', 0, sep='')