import sys

sys.stdin = open("_암호생성기.txt")

for C in range(1, 11): 
    T = int(input())
    matrix_2 = input().split()
    count = 0
    while int(matrix_2[7]) > 0:
        count = 0
        for i in range(5):
            count += 1
            matrix_2.pop(0)
            if (int(N) - count) <= 0:
                matrix_2.append(0)
                break
            else:
                matrix_2.append(int(N) - count)
    print(f'#{C}', matrix_2)
    
    

