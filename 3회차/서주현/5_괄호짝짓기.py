import sys

sys.stdin = open("_괄호짝짓기.txt")

for i in range(1, 11) :
    t = int(input())

    brackets = list(input())
    stack = []
    lbra = ['(', '[', '{', '<']
    rbra = [')', ']', '}', '>']

    its = True
    for j in brackets :
        # print(j)
        if j in lbra :
            stack.append(j)
            
        else :
            for k in range(4) :
                if j == rbra[k] :
                    idx = k
                    break
            
            if stack[-1] == lbra[idx] :
                stack.pop()
            else :
                its = False
                break

        if its == False :
            break
    if stack == [] and its == True:
        print(f'#{i}', 1)
    else :
        print(f'#{i}', 0)


    # break