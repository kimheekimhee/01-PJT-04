import sys

sys.stdin = open("_암호생성기.txt")

for i in range(10):
    T = int(input())
        
    numbers = list(map(int, input().split()))

    while numbers[7] != 0:
        for j in range(1, 6):
            pop_num = numbers.pop(0)
            if pop_num - j <= 0:
                numbers.append(0)
                break
            else:
                numbers.append(pop_num - j)

    result = ' '.join(map(str, numbers))
    print(f'#{T} {result}')