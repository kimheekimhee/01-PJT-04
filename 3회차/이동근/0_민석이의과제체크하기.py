T = int(input())

for i in range(T):
    N, K = map(int, input().split())

    # 집합에서 차집합 이용
    ret = set([i for i in range(1, N + 1)]) - set(list(map(int, input().split())))

    print(f"#{i + 1}", *sorted(ret))