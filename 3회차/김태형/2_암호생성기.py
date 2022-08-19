# import sys

# sys.stdin = open("_암호생성기.txt")

# A = [9550,9556,9550,9553,9558,9551,9551,9551]
A = [10,6,12,8,9,4,1,3]

while A[7]!=0:
    i=0
    while i<=5:
        i+=1 # 
        print(A)
        A.append(A[0]-i)
        A.remove(A[0])
        if A[7]==0:
            break
print(A)
