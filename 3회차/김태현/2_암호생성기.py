import sys
sys.stdin = open("_암호생성기.txt")


for _ in range(10):
    case_num = int(input())
    num_li = list(map(int, input().split()))

    i = 1
    while True:
        if i > 5:
            i = 1
        num_li[0] -= i
        if num_li[0] <= 0:
            num_li.append(0)
            del num_li[0]
            break
        num_li.append(num_li[0])
        del num_li[0]
        i += 1
    print(f"#{case_num}", *num_li)

        