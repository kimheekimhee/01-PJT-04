# import sys

# sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for _ in range(1, T+1):
    N, K = map(int, input().split()) # 5, 3
    submit = input().split() # ['2', '5', '3']
    a = []
    for i in range(1, N+1): # 1, 2, 3, 4, 5
        a.append(str(i))
    
    for j in range(len(submit)):
        if submit[j] in a:
            a.remove(submit[j])


    print("#{} {}".format(_, ' '.join(a)))
    
        
