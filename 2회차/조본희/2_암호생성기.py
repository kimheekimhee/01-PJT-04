import sys

sys.stdin = open("_암호생성기.txt")

for test_case in range(1, 11):
    t = int(input())
    numbers = list(map(int, input().split()))

    subnum = 1
    while True:
        temp = numbers.pop(0)           #첫번째 숫자를 빼서 저장해두기
        if temp - subnum <= 0:          #탈출 조건문
            numbers.append(0)
            break

        numbers.append(temp - subnum)
        subnum += 1
        if subnum > 5:                  #-5까지 순회하면 다시 1로 초기화
            subnum = 1

    print(f'#{t} {" ".join(map(str, numbers))}')