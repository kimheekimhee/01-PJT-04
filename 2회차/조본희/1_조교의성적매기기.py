import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    score = []
    for i in range(N):
        a, b, c = map(int, input().split())
        score.append(a*35 + b*45 + c*20)

    mult = N // 10
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    
    result = [''] * N  
    for i in range(10):
        for j in range(mult):
            idx = score.index(max(score))
            result[idx] = grade[i]
            score[idx] = -1
    print(f'#{test_case} {result[K-1]}')
