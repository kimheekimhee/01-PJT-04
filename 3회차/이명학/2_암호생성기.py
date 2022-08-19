import sys

sys.stdin = open(
    "C:\\Users\\이명학\\Desktop\\멀티캠퍼스\\01-PJT-04\\3회차\\이명학\\_암호생성기.txt")

T = 10
for _ in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))  # 8개의 숫자를 입력 받음
    roop = False

    while 1:
        # 제일 앞의 숫자를 기준으로 1씩 커지는 숫자를 뺌
        for k in range(1, 6):
            secret_number = arr.pop(0) - k  # 처음 인덱스와 - k 값을 secret_number에 저장
            # 뺀 숫자가 0보다 큰 경우는 맨 뒤에 숫자를 추가
            if secret_number > 0:
                arr.append(secret_number)
            # 뺀 숫자가 0인경우 맨 뒤에 0을 추가하고 종료
            else:
                arr.append(0)
                roop = True
                break
        if roop:
            break
    print(f"#{_}", end=" ")
    print(*arr)
