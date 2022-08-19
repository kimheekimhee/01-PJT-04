import sys

sys.stdin = open("_민석이의과제체크하기.txt")
T = int(input())
for test_case in range(1,T+1):
    n,sub = map(int,input().split())
    std_set = set()
    sub_list = list(map(int,input().split()))
    sub_lsit = set(sub_list)
    for s in range(1,n+1):
        std_set.add(s)
    result = set.difference(std_set,sub_list)
    result = list(result)
    result = map(str,result)
    result = ' '.join(result)

    print(f'#{test_case}',result)