
for i in range(10):

    t = int(input())
    numlist = list(map(int,input().split()))
    i = 0
    while True:
        i += 1
        num = numlist[0] - i
        if num <= 0:
            num = 0
            numlist.append(num)
            del numlist[0]
            break
        numlist.append(num)
        del numlist[0]

        if i == 5:
            i = 0

    print(f'#{t}', *numlist)