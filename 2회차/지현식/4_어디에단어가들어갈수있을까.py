import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

for test_case in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    maps = [list(map(str, input().split())) for _ in range(n)]
    # maps 의 열을 행으로 전환
    maps2 = list(map(list, zip(*maps)))
    # 카운트 하기 위한 변수
    cnt = 0
    # 각 행이 k 만큼길이가 있는지 없는지 확인 이후 k 만큼있으면 +1
    for i in maps:
        cnt += ''.join(i).split('0').count('1' * k)

    # 각 행이 k 만큼길이가 있는지 없는지 확인 이후 k 만큼있으면 +1
    for i in maps2:
        cnt += ''.join(i).split('0').count('1' * k)
    print(f"#{test_case} {cnt}")