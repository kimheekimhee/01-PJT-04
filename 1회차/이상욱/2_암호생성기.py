import sys
sys.stdin = open("_암호생성기.txt")

numbers = [9550, 9556, 9550, 9553, 9558, 9550, 9551, 9551]
while True:
    for i in range(1, 6):
        num = numbers.pop(0)
        numbers.append(num - i)

print(numbers)