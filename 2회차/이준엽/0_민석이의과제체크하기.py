t = int(input())
for _ in range(1,t+1):
    n,k = map(int,input().split())
    numbers = list(map(int,input().split()))
    no_push = list(range(1,n+1))
    for i in numbers:
        if i in range(1,n+1):
            no_push.remove(i)
    print(f'#{_}',*no_push)
        