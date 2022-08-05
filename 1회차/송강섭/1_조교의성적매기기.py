import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())
for test_case in range(1, T+1):
    # n = 학생수, k = 학점확인
    n, k = map(int, input().split())
    arr = []
    for i in range(1, n+1):
        a, b, c = map(float, input().split())
        d = (a * 0.35) + (b * 0.45) + (c * 0.2)
        arr.append(d)
        sorted(arr)
        cnt = len(arr)
        num = cnt % 10
    if cnt == 10:
        arr[0] = 'A+'
        arr[1] = 'A0'
        arr[2] = 'A-'
        arr[3] = 'B+'
        arr[4] = 'B0'
        arr[5] = 'B-'
        arr[6] = 'C+'
        arr[7] = 'C0'
        arr[8] = 'C-'
        arr[9] = 'D0'
print(arr[k])
