import sys

sys.stdin = open("_파리퇴치.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    length, hit = map(int, input().split())
    seet = []
    for _ in range(length):
        line = list(map(int, input().split()))
        seet.append(line)
    max = 0

    for i in range(length - hit + 1):
        for j in range(length - hit + 1):
            fly = 0
            for i2 in range(hit):
                for j2 in range(hit):
                    fly += seet[i + i2][j + j2]
            if fly > max:
                max = fly
    
    print(f'#{test} {max}')