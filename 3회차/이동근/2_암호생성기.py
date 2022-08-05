for _ in range(10):
    T = int(input())

    line = list(map(int, input().split()))

    # 복사본을 만들기 위해서 슬라이싱을 이용했다.
    cycle = line[:]
    i = 1
    while cycle[-1] != 0:
        val = 0 if cycle[0] - i < 1 else cycle[0] - i
        cycle = cycle[1:]
        cycle.append(val)
        i = i + 1 if i < 5 else 1

    print(f"#{T}", *cycle)