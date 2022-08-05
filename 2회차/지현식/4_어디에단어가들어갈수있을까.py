import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

for test_case in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    maps = [list(map(str, input().split())) for _ in range(n)]
    maps2 = list(map(list, zip(*maps)))
    cnt = 0

    for i in maps:
        cnt += ''.join(i).split('0').count('1' * k)

    for i in maps2:
        cnt += ''.join(i).split('0').count('1' * k)
    print(f"#{test_case} {cnt}")