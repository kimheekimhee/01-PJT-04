grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    K -= 1

    ret = []
    for j in range(N):
        mid, end, hw = map(int, input().split())

        mid *= 0.35
        end *= 0.45
        hw *= 0.2

        ret.append(mid + end + hw)

    # 정렬 후 원본 순서를 기억 해야하므로 enumerate 를 사용했다.
    rank = sorted(enumerate(ret), key=lambda x: x[1], reverse=True)

    for j in rank:
        if j[0] == K:
            idx = rank.index(j)
            rate = N // 10
            print(f"#{i + 1}", grade[idx // rate])