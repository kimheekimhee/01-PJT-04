
T = int(input())

for TC in range(1, T + 1):
    N, K = map(int, input().split())
    Submitted = list(map(int, input().split()))
    F_list = []

    for i in range(1, N + 1) :
        if i not in Submitted:
            F_list.append(i)
    
    print(f'#{TC} {F_list}') # I cannot remove bracket from the list 'F_list'
    