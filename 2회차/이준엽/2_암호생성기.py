for i in range(10):
    t = int(input())
    numbers = list(map(int,input().split()))
    cnt=1
    while True:
        if numbers[0] - cnt <=0:
            numbers.pop(0)
            numbers.append(0)
            break
        numbers.append(numbers.pop(0)-cnt)
        cnt+=1
        if cnt>5:
            cnt=1
    print(f'#{t}',*numbers)