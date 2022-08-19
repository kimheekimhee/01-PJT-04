import sys

sys.stdin = open("_괄호짝짓기.txt")
for i in range(10):
    length=int(input())
    Word=list(input())
    j=0
    while 1:
        if j==length-1:
            break
        if Word[j]=='(':
            k=j
            while 1:
                if k == length-1:
                    break
                if Word[k+1]==')':
                    Word[j]='0'
                    Word[k+1]='0'
                    break
                else:
                    k+=1
            j+=1
        elif Word[j]=='[':
            k=j
            while 1:
                if k == length-1:
                    break
                if Word[k+1]==']':
                    Word[j]='0'
                    Word[k+1]='0'
                    break
                else:
                    k+=1
            j+=1
        elif Word[j]=='{':
            k=j
            while 1:
                if k == length-1:
                    break
                if Word[k+1]=='}':
                    Word[j]='0'
                    Word[k+1]='0'
                    break
                else:
                    k+=1
            j+=1
        elif Word[j]=='<':
            k=j
            while 1:
                if k == length-1:
                    break
                if Word[k+1]=='>':
                    Word[j]='0'
                    Word[k+1]='0'
                    break
                else:
                    k+=1
            j+=1
        elif Word[j] =='0':
            j+=1
        else:
            break      
    cnt=0    
    for n in range(len(Word)):
        if Word[n] =='0':
            cnt+=1
    if cnt != length:
        print(f'#{i+1} {0}')
    else:
        print(f'#{i+1} {1}')