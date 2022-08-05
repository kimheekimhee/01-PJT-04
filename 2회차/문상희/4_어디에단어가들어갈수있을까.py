import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    size, length = map(int, input().split())
    
    seet = []
    for _ in range(size):
        line = list(map(int, input().split()))
        seet.append(line)
    
    right = 0
    for i in range(size):
        word = 0
        for j in range(size):
            if seet[i][j] == 1:
                word += 1
            else:
                if word == length:
                    right += 1
                    word = 0
                else:
                    word = 0
        if word == length:
            right += 1

    for i in range(size):
        word = 0
        for j in range(size):
            if seet[j][i] == 1:
                word += 1
            else:
                if word == length:
                    right += 1
                    word = 0
                else:
                    word = 0
        if word == length:
            right += 1
 
            
    print(f'#{test} {right}')