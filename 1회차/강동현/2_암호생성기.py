import sys

sys.stdin = open("_암호생성기.txt")

# recursion error
def cycle(lst):
    for i in range(1,6):
        if lst[0]-i>0:
            lst.append(lst[0]-i)
            lst.pop(0)
        else:
            lst.append(0)
            lst.pop(0)
            lst = map(str,lst)
            return lst
    return cycle(lst)

for i in range(10):
    num = int(input())
    old = list(map(int,input().split()))
    pwd = cycle(old)
    print(f'#{num} {" ".join(pwd)}')

# New Sol
while True:
    try:
        num = int(input())
        pwd = list(map(int, input().split()))
        i= 1
        while True:
            if i>5:
                i=1
            chk = pwd.pop(0)-i
            if chk>0:
                pwd.append(chk)
            else:
                pwd.append(0)
                break
            i += 1
        pwd = map(str, pwd)
        newnum = ' '.join(pwd)
        print(f'#{num} {newnum}')
    except EOFError:
        break