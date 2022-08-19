import sys

sys.stdin = open("_조교의성적매기기.txt")
T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for i in range(1, T+1):
    a, k = map(int, input().split())
    result = []
    for j in range(a):
        b, c, d = map(int, input().split())
        average = (b * 0.35) + (c * 0.45) + (d * 0.20)
        result.append(average)
    kk = result[k-1]
    result.sort(reverse=True)
    N = a//10
    kgrade = result.index(kk) // N
    print(f'#{i}', grade[kgrade])