import sys

sys.stdin = open("_괄호짝짓기.txt")
N=10
a=[]
for _ in range(N):
    n=input()
    T=input()
    print(T)
    for i in T:
        if i=='(':
            a.append(i)
        else: 
            if i=='{':
                a.append(i)
            else:
                if i=='<':
                    a.append(i)
                else: 
                    if i=='[':
                        a.append(i)


    print(a)
    if len(a)==0 and len(T)==0:
        print(f'#{N} 1')
    else: print(f'#{N} 0')