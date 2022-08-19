braket = ["()", "[]", "{}", "<>"]

for i in range(10):
    len = int(input())

    line = input()
    cp = line[:]

    # 이전에 백준에서 본 코드가 기억이 난다.
    # 해당 문제 풀이 중 가장 간결한 코드를 사용했다.
    for j in line:
        for k in braket:
            if j in k:
                cp = cp.replace(k, "")

    print(f"#{i + 1}", 1 if not cp else 0)