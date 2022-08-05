import sys

sys.stdin = open("_민석이의과제체크하기.txt")
t = int(input())

for i in range(t):
    ans = []
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    # 입력 값에서 없는 수를 리스트에 추가
    for j in range(1, n + 1):
        if j not in arr:
            ans.append(j)

    print(f'#{i + 1} {(" ".join(map(str, ans)))}')
    