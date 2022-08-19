T = int(input())
for tc in range(1, T + 1):
    result = []
    total, submit_cnt = input().split()
    for i in range(1, int(total)+1):
        result.append(str(i))
    submit = input().split()
    
    for j in submit:
        if j in result:
            result.remove(j)

    print(f"#{tc} {' '.join(result)}")