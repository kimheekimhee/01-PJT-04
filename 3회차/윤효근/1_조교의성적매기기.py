import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_case in range(1, T + 1):
    a,n = map(int,input().split())
    result = []


    for _ in range(a):
        m,f,h=map(int,input().split())
        Total = (m * 0.35)+(f * 0.45)+(h * 0.20)
        result.append(Total)

    n_score=result[n-1]

    result.sort(reverse=True)

    duple = a//10
    fn_score=result.index(n_score)//duple


    print(f'#{test_case} {grades[fn_score]}')
