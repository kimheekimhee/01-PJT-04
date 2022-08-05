# import sys

# sys.stdin = open("_암호생성기.txt")

A = [9550,9556,9550,9553,9558,9551,9551,9551]
while A:
    for i in range(1,5):
        A.append(A[0]-i)
        A.remove(A[0])
    if A[7]==0:
        break
print(A)
