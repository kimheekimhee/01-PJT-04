import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

for i in range(1, T + 1):
    N, K = map(int, input().split())

    grades = dict()
    for student in range(1, N + 1):
        temp = list(map(float, input().split()))
        grades[student] = (temp[0] * 0.35) + (temp[1] * 0.45) + (temp[2] * 0.2)

    rank = []
    for grade in grades:
        rank.append(grades[grade])
    rank.sort()
    rank = rank[::-1]
        
    divide = N // 10
    if grades[K] >= rank[divide - 1]:
        print(f'#{i}', 'A+')
    elif grades[K] >= rank[divide * 2 - 1]:
        print(f'#{i}', 'A0')
    elif grades[K] >= rank[divide * 3 - 1]:
        print(f'#{i}', 'A-')
    elif grades[K] >= rank[divide * 4 - 1]:
        print(f'#{i}', 'B+')
    elif grades[K] >= rank[divide * 5 - 1]:
        print(f'#{i}', 'B0')
    elif grades[K] >= rank[divide * 6 - 1]:
        print(f'#{i}', 'B-')
    elif grades[K] >= rank[divide * 7 - 1]:
        print(f'#{i}', 'C+')    
    elif grades[K] >= rank[divide * 8 - 1]:
        print(f'#{i}', 'C0')
    elif grades[K] >= rank[divide * 9 -1]:
        print(f'#{i}', 'C-')
    else:
        print(f'#{i}', 'D0')