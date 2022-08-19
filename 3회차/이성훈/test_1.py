import sys

sys.stdin = open("test.txt")

T = int(input())

for j in range(1, T+1):

    N, K = map(int, input().split())
    Z = int(N/10)
    N_list = []


    for i in range(N):
        N1, N2, N3 = map(int, input().split())
        N1 *= 0.35
        N2 *= 0.45
        N3 *= 0.2
        N4 = [(N1), (N2), (N3)]
        N_list.append(sum(N4))

    sort_N_list = sorted(N_list)[::-1]

    for i in range(N):
        if N_list[i] >= sort_N_list[Z-1]:
            N_list[i] = 'A+'

        elif N_list[i] >= sort_N_list[2*Z-1]:
            N_list[i] = 'A0'

        elif N_list[i] >= sort_N_list[3*Z-1]:
            N_list[i] = 'A-'

        elif N_list[i] >= sort_N_list[4*Z-1]:
            N_list[i] = 'B+'

        elif N_list[i] >= sort_N_list[5*Z-1]:
            N_list[i] = 'B0'

        elif N_list[i] >= sort_N_list[6*Z-1]:
            N_list[i] = 'B-'

        elif N_list[i] >= sort_N_list[7*Z-1]:
            N_list[i] = 'C+'

        elif N_list[i] >= sort_N_list[8*Z-1]:
            N_list[i] = 'C0'

        elif N_list[i] >= sort_N_list[9*Z-1]:
            N_list[i] = 'C-'

        elif N_list[i] >= sort_N_list[10*Z-1]:
            N_list[i] = 'D0'


    print(f'#{j}', N_list[K-1])